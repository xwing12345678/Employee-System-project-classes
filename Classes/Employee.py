
class Employee:
    def __init__(self,name:str,salary:int|float) -> None:
        self.__name, self.__salary = name,salary

    def title(self)->str:
        return "Employee"

    @property
    def salary(self)->int|float:
        return self.__salary
    
    def monthly_cost(self)->int|float:
        return self.__salary

    def describe(self)->str:
        return self.__name + " (" + self.title() + "): " + str(self.monthly_cost())


    
    
    
    
    
    
    
    @property
    def name(self)->str:
        return self.__name
