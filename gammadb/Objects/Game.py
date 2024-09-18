class Game:
	def __init__(self,game_id:int|None,name:str,thumbnail_id:int,banner_id:int|None,short_description:str,long_description:str,location_id:int,parent_directory:str,launch_type:int=1,game_launch_file:str="Game.exe",launch_arguments:str="",last_played:str="Never",minutes_on_record:int=0,game_type:int=1,version_major:int=1,version_minor:int=0,version_revision:int=0) -> None:
		self.__id:int|None = game_id
		self.__name:str = name
		self.__thumbnail_id:int = thumbnail_id
		self.__banner_id:int|None = banner_id
		self.__short_description:str = short_description
		self.__long_description:str = long_description
		self.__location_id:int = location_id
		self.__parent_directory:str = parent_directory
		self.__launch_type:int = launch_type
		self.__game_launch_file:str = game_launch_file
		self.__launch_arguments:str = launch_arguments
		self.__last_played:str = last_played
		self.__minutes_on_record:int = minutes_on_record
		self.__game_type:int = game_type
		self.__version_major:int = version_major
		self.__version_minor:int = version_minor
		self.__version_revision:int = version_revision
	
	@property
	def ID(self) -> int|None:
		return self.__id
	@ID.setter
	def ID(self,new_id:int) -> None:
		self.__id = new_id
	
	@property
	def Name(self) -> str:
		return self.__name
	
	@property
	def ThumbnailID(self) -> int:
		return self.__thumbnail_id
	
	@property
	def BannerID(self) -> int|None:
		return self.__banner_id
	@BannerID.setter
	def BannerID(self,new_id:int) -> None:
		self.__banner_id = new_id
	
	@property
	def ShortDescription(self) -> str:
		return self.__short_description
	
	@property
	def LongDescription(self) -> str:
		return self.__long_description
	
	@property
	def LocationID(self) -> int:
		return self.__location_id
	
	@property
	def ParentDirectory(self) -> str:
		return self.__parent_directory
	
	@property
	def LaunchType(self) -> int:
		return self.__launch_type
	
	@property
	def GameLaunchFile(self) -> str:
		return self.__game_launch_file
	
	@property
	def LaunchArguments(self) -> str:
		return self.__launch_arguments
	
	@property
	def LastPlayed(self) -> str:
		return self.__last_played
		
	@property
	def MinutesOnRecord(self) -> int:
		return self.__minutes_on_record
	
	@property
	def GameType(self) -> int:
		return self.__game_type
	
	@property
	def VersionMajor(self) -> int:
		return self.__version_major
	
	@property
	def VersionMinor(self) -> int:
		return self.__version_minor
	
	@property
	def VersionRevision(self) -> int:
		return self.__version_revision
