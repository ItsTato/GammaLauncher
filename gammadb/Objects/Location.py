class Location:
	def __init__(self,location_id:int|None,name:str,path:str,game_amount:int=0) -> None:
		self.__id:int|None = location_id
		self.__name:str = name
		self.__path:str = path
		self.__game_amount:int = game_amount

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
	def Path(self) -> str:
		return self.__path
	
	@property
	def GameAmount(self) -> int:
		return self.__game_amount
