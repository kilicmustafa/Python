class Person:
    def __init__(self,FirstName,LastName,Age):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age


class Worker(Person):
    def __init__(self,Salary):
        self.Salary = Salary

class Customer(Person):
    def __init__(self,CrediCardNumber):
        self.CrediCartNumbers = CrediCardNumber


Customer.Age = 33
