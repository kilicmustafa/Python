class Person:
    def __init__(self,FirstName,LastName,Age):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age

person1 = Person("Mustafa","Kılıç",18)
print(person1.FirstName)