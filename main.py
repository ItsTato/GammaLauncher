import flask
from os import path
from json import load, dumps
import subprocess
from time import sleep
from threading import Thread

from gammadb import Controller
from gammadb.Objects import Game, Image, Location

with open("./config.json","r") as file:
	config:dict = load(file)

version:str = f"{config['Version']['Major']}.{config['Version']['Minor']}.{config['Version']['Revision']}{'a' if config['Version']['Channel'] == 'alpha' else 'b' if config['Version']['Channel'] == 'beta' else '' if config['Version']['Channel'] == 'release' else 'u'}"
print(f"GammaLauncher {version}")

database:Controller = Controller("./data/GammaData.db3")

flask_path:str = path.join("./","flask")
site:flask.Flask = flask.Flask(__name__)

gameTracking:dict[int,subprocess.Popen] = {
	#1: process
}

@site.route("/",methods=["GET"])
def index():
	return "Hello, world!"

@site.route("/images/<image_id>",methods=["GET"])
def get_image(image_id:int):
	image:Image|None = database.getImage(image_id)
	if image is None:
		return "Invalid image id!"
	return flask.send_file(f"data/images/{image.ID}.{image.FileExtension}")

@site.route("/images/profile_picture",methods=["GET"])
def get_profile_picture():
	return flask.send_file(f"data/images/{config['User']['Profile Picture']}")

@site.route("/api/games",methods=["GET"])
def list_games():
	games:list[Game] = database.getAllGames()
	gamesList:list[dict[str,str|int|None|dict[str,int]]] = []
	for game in games:
		gamesList.append({
			"ID": game.ID,
			"Name": game.Name,
			"ThumbnailID": game.ThumbnailID,
			"BannerID": game.BannerID,
			"ShortDescription": game.ShortDescription,
			"LongDescription": game.LongDescription,
			"LocationID": game.LocationID,
			"ParentDirectory": game.ParentDirectory,
			"LaunchType": game.LaunchType,
			"GameLaunchFile": game.GameLaunchFile,
			"LaunchArguments": game.LaunchArguments,
			"LastPlayed": game.LastPlayed,
			"MinutesOnRecord": game.MinutesOnRecord,
			"GameType": game.GameType,
			"Version": {
				"Major": game.VersionMajor,
				"Minor": game.VersionMinor,
				"Revision": game.VersionRevision
			}
		})
	return flask.make_response(dumps(gamesList),200)

@site.route("/games",methods=["GET"])
def games():
	return flask.render_template("games.html",username=config["User"]["Username"])

@site.route("/games/<game_id>",methods=["GET"])
def view_game(game_id:int):
	game:Game|None = database.getGame(game_id)
	if game is None:
		return "Invalid game id!"
	return flask.render_template("game.html",game=game,username=config["User"]["Username"])

@site.route("/games/<game_id>/launch",methods=["POST"])
def launch_game(game_id:int):
	game:Game|None = database.getGame(game_id)
	if game is None:
		return flask.make_response("Invalid game id!",404)
	location:Location|None = database.getLocation(game.LocationID)
	if location is None:
		return flask.make_response("Invalid location id! Please check your database!",404)
	if game.LaunchType == 1:
		game_file_path:str = f"{location.Path}/{game.ParentDirectory}/{game.GameLaunchFile}"
		gameTracking[game.ID] = subprocess.Popen(#type:ignore
			args=[game.LaunchArguments] if not game.LaunchArguments is None else [],
			executable=game_file_path,
			stdout=subprocess.DEVNULL,
			stderr=subprocess.DEVNULL
		)
	return flask.make_response("Running",200)

@site.route("/games/<game_id>/kill",methods=["POST"])
def kill_game(game_id:int):
	game_id = int(game_id)
	if game_id in gameTracking:
		if gameTracking[game_id].poll() is None:
			gameTracking[game_id].kill()
		else:
			gameTracking.pop(game_id)
	return flask.make_response("Killed",200)

@site.route("/games/<game_id>/status",methods=["GET"])
def game_status(game_id:int):
	game_id = int(game_id)
	running:bool = False
	if game_id in gameTracking:
		if gameTracking[game_id].poll() is None:
			running = True
		else:
			gameTracking.pop(game_id)
	return dumps({
		"Running": running
	})

site.run(host="0.0.0.0",port=4242)
