class MyClass:
    
    #Private method
    def registry(self) -> None:
        print("Started process")
        self.__verify()
        self.__verify_registry()
        self.__insert_data()
        
    #Public methods
    def __verify(self) -> None:
        print("Verify data")
    
    def __verify_registry(self) -> None:
        print("Verify registry")
        
    def __insert_data(self) -> None:
        print("Insert in DB")
        
obj = MyClass()
obj.registry()