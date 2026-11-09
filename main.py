from Classes.Employee import Employee
from Classes.Manager import Manager
from Classes.Intern import Intern
from typing import Literal

Month_Number = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


staff = [
    Employee("Dana", 12000),
    Manager("Avi", 20000, 3000),
    Intern("Noa", 6000, 6),
]

for person in staff:
    print(person.describe())

try:
    Intern("Tom", 5000, 0)
except ValueError as error:
    print("error:", error)
total = 0
for person in staff:
    total = total + person.monthly_cost()
print("Total monthly cost:", total)