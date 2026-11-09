from .Employee import Employee
from typing import Literal

Month_Number = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

class Intern(Employee):
        def __init__(self,name:str,salary:int|float,months:Month_Number) -> None:
            if months not in range(1, 13):
                raise ValueError("months must be 1-12")
            super().__init__(name, salary)
            self.__months = months

        def title(self)->str:
            return "Intern"