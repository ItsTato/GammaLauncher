import flask
from os import path
from json import load

from gammadb import Controller
from gammadb.Objects import Game, Image

with open("./config.json","r") as file:
	config:dict = load(file)

version:str = f"{config['Version']['Major']}.{config['Version']['Minor']}.{config['Version']['Revision']}{'a' if config['Version']['Channel'] == 'alpha' else 'b' if config['Version']['Channel'] == 'beta' else '' if config['Version']['Channel'] == 'release' else 'u'}"
print(version)

database:Controller = Controller("./data/GammaData.db3")

flask_path:str = path.join("./","flask")
site:flask.Flask = flask.Flask(__name__)

@site.route("/",methods=["GET"])
def index():
	return "Hello, world!"

@site.route("/images/<image_id>",methods=["GET"])
def get_image(image_id:int):
	image:Image|None = database.getImage(image_id)
	if image is not None:
		return flask.send_file(f"data/images/{image.ID}.{image.FileExtension}")
	return "Invalid image id!"

@site.route("/images/profile_picture",methods=["GET"])
def get_profile_picture():
	return flask.send_file(f"data/images/{config['Profile Picture']}")

@site.route("/games",methods=["GET"])
def games():
	return "Games list here.."

@site.route("/games/<game_id>",methods=["GET"])
def view_game(game_id:int):
	game:Game|None = database.getGame(game_id)
	if game is not None:
		return flask.render_template("game.html",game=game)
	return "Invalid game id!"

site.run(host="0.0.0.0",port=4242)
