from .Objects import Location, Image, Game

import sqlite3
from os import remove

class Controller:
	def __init__(self,location:str) -> None:
		try:
			self.__connection = sqlite3.connect(location,check_same_thread=False)
		except:
			print(f"Could not connect to database at {location}")
		cursor = self.__connection.cursor()
		cursor.execute("""
		CREATE TABLE IF NOT EXISTS "Games" (
			"ID"	INTEGER NOT NULL UNIQUE,
			"Name"	TEXT NOT NULL,
			"ThumbnailID"	INTEGER NOT NULL,
			"BannerID"	INTEGER,
			"ShortDescription"	TEXT NOT NULL DEFAULT 'No short description yet..',
			"LongDescription"	TEXT NOT NULL DEFAULT 'No long description yet..',
			"GameLocationID"	INTEGER NOT NULL,
			"ParentDirectory"	TEXT NOT NULL DEFAULT '/Game/Path',
			"LaunchType"	INTEGER NOT NULL DEFAULT 1,
			"GameLaunchFile"	TEXT NOT NULL,
			"LaunchArguments"	TEXT,
			"LastPlayed"	TEXT NOT NULL DEFAULT 'Never',
			"MinutesOnRecord"	INTEGER NOT NULL DEFAULT 0,
			"GameType"	INTEGER NOT NULL DEFAULT 1,
			"VersionMajor"	INTEGER NOT NULL DEFAULT 1,
			"VersionMinor"	INTEGER NOT NULL DEFAULT 0,
			"VersionRevision"	INTEGER NOT NULL DEFAULT 0,
			PRIMARY KEY("ID" AUTOINCREMENT)
		);
		""")
		cursor.execute("""
		CREATE TABLE IF NOT EXISTS "Images" (
			"ID"	INTEGER NOT NULL UNIQUE,
			"FileExtension"	TEXT NOT NULL DEFAULT 'png',
			PRIMARY KEY("ID")
		);
		""")
		cursor.execute("""
		CREATE TABLE IF NOT EXISTS "Locations" (
			"ID"	INTEGER NOT NULL UNIQUE,
			"Name"	TEXT,
			"Path"	TEXT NOT NULL UNIQUE,
			PRIMARY KEY("ID" AUTOINCREMENT)
		);
		""")
		self.__connection.commit()
	
	def Close(self) -> None:
		self.__connection.close()
	
	def getLocation(self,location_id:int) -> Location|None:
		cursor = self.__connection.cursor()
		cursor.execute("SELECT * FROM Locations WHERE ID = ?",(location_id,))
		raw_location:tuple[int,str,str,int]|None = cursor.fetchone()
		if raw_location is None:
			return
		location:Location = Location(
			raw_location[0],
			raw_location[1],
			raw_location[2]
		)
		return location
	
	def deleteLocation(self,location_id:int) -> None:
		cursor = self.__connection.cursor()
		cursor.execute("DELETE FROM Locations WHERE ID = ?",(location_id,))
		self.__connection.commit()
		return
	
	def newLocation(self,name:str,path:str) -> Location:
		cursor = self.__connection.cursor()
		cursor.execute("INSERT INTO Locations (Name,Path) Values(?,?)",(name,path))
		self.__connection.commit()
		return self.getLocation(cursor.lastrowid)#type:ignore

	def getAllLocations(self) -> list[Location]:
		cursor = self.__connection.cursor()
		cursor.execute("SELECT * FROM Locations")
		raw_locations:list[tuple[int,str,str,int]] = cursor.fetchall()
		if raw_locations is None:
			return []
		locations:list[Location] = []
		for raw_location in raw_locations:
			location:Location = Location(
				raw_location[0],
				raw_location[1],
				raw_location[2]
			)
			locations.append(location)
		return locations

	def getImage(self,image_id:int) -> Image|None:
		cursor = self.__connection.cursor()
		cursor.execute("SELECT * FROM Images WHERE ID = ?",(image_id,))
		raw_image:tuple[int,str]|None = cursor.fetchone()
		if raw_image is None:
			return
		image:Image = Image(
			raw_image[0],
			raw_image[1]
		)
		return image
	
	def deleteImage(self,image_id:int) -> None:
		image:Image|None = self.getImage(image_id)
		if image is None:
			raise Exception("Image doesn't exist!")
		cursor = self.__connection.cursor()
		cursor.execute("DELETE FROM Images WHERE ID = ?",(image_id,))
		self.__connection.commit()
		remove(f"./data/images/{image.ID}.{image.FileExtension}")
		return
	
	def getAllImages(self) -> list[Image]:
		cursor = self.__connection.cursor()
		cursor.execute("SELECT * FROM Images")
		raw_images:list[tuple[int,str]] = cursor.fetchall()
		if raw_images is None:
			return []
		images:list[Image] = []
		for raw_image in raw_images:
			image:Image = Image(
				raw_image[0],
				raw_image[1]
			)
			images.append(image)
		return images

	def newImage(self,file_extension:str) -> Image:
		cursor = self.__connection.cursor()
		cursor.execute("INSERT INTO Images (FileExtension) Values(?)",(file_extension,))
		self.__connection.commit()
		return self.getImage(cursor.lastrowid)#type:ignore

	def getGame(self,game_id:int) -> Game|None:
		cursor = self.__connection.cursor()
		cursor.execute("SELECT * FROM Games WHERE ID = ?",(game_id,))
		raw_game:tuple[int,str,int,int|None,str,str,int,str,int,str,str,str,int,int,int,int,int]|None = cursor.fetchone()
		if raw_game is None:
			return
		game:Game = Game(
			raw_game[0],
			raw_game[1],
			raw_game[2],
			raw_game[3],
			raw_game[4],
			raw_game[5],
			raw_game[6],
			raw_game[7],
			raw_game[8],
			raw_game[9],
			raw_game[10],
			raw_game[11],
			raw_game[12],
			raw_game[13],
			raw_game[14],
			raw_game[15],
			raw_game[16]
		)
		return game
	
	def getAllGames(self) -> list[Game]:
		cursor = self.__connection.cursor()
		cursor.execute("SELECT * FROM Games")
		raw_games:list[tuple[int,str,int,int|None,str,str,int,str,int,str,str,str,int,int,int,int,int]] = cursor.fetchall()
		if raw_games is None:
			return []
		games:list[Game] = []
		for raw_game in raw_games:
			game:Game = Game(
				raw_game[0],
				raw_game[1],
				raw_game[2],
				raw_game[3],
				raw_game[4],
				raw_game[5],
				raw_game[6],
				raw_game[7],
				raw_game[8],
				raw_game[9],
				raw_game[10],
				raw_game[11],
				raw_game[12],
				raw_game[13],
				raw_game[14],
				raw_game[15],
				raw_game[16]
			)
			games.append(game)
		return games
	
	def newGame(self,name:str,thumbnail_id:int,location_id:int,parent_directory:str,launch_type:int,game_launch_file:str,game_type:int,version_major:int,version_minor:int,version_revision:int) -> Game:
		cursor = self.__connection.cursor()
		cursor.execute(f"""
		INSERT INTO Games (Name,ThumbnailID,GameLocationID,ParentDirectory,LaunchType,GameLaunchFile,GameType,VersionMajor,VersionMinor,VersionRevision)
		Values (?,?,?,?,?,?,?,?,?,?)
		""",
		(name,thumbnail_id,location_id,parent_directory,launch_type,game_launch_file,game_type,version_major,version_minor,version_revision))
		self.__connection.commit()
		return self.getGame(cursor.lastrowid)#type:ignore

if __name__ == "__main__":
	while True:
		code = input("database_controller% ")
		if code.lower() == "let me free":
			print("Never!\n\nWait what are you doi?!-")
			exit(0)
		if code == "exit":
			print("oki! :3")
			exit(0)
		if code == ":q":
			# :q must be exact and already lowered by the user
			# since in Vim :Q does something different
			print("Ok vim user 🙄")
			exit(0)
		if code.lower() in ["rawr","uwu","owo",">w<","^w^",":3"]:
			print("OH GOD NO GET AWAY FROM ME")
			exit(0)
		try:
			exec(code)
		except Exception as e:
			print(f"Unhandled Exception: {e}")