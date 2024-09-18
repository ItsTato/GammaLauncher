class Image:
	def __init__(self,image_id:int|None,image_type:int=1,file_extension:str="png") -> None:
		self.__image_id:int|None = image_id
		self.__image_type:int = image_type
		self.__file_extension:str = file_extension

	@property
	def ID(self) -> int|None:
		return self.__image_id
	@ID.setter
	def ID(self,new_id:int) -> None:
		self.__image_id = new_id
	
	@property
	def ImageType(self) -> int:
		return self.__image_type
	
	@property
	def FileExtension(self) -> str:
		return self.__file_extension
