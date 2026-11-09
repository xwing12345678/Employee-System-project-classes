
from .Employee import Employee

class Manager(Employee):
        def __init__(self,name:str,salary:int|float,bonus:int|float) -> None:
            super().__init__(name, salary)
            self.__bonus = bonus

        def monthly_cost(self)->int|float:
            regular_pay:int|float = super().monthly_cost()
            return regular_pay + self.__bonus

        def title(self)->str:
            return "Manager"
        



 