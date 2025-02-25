class Person:
    def __init__(self, name, age,salary):
        self.name = name
    #public attribute
        self.age = age
    #protected attribute
        self.salary = salary
    #private attribute

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self.salary)

person1=Person("Justin",36,20000)
person1.display()
print("Accessing attributes outside class:")
print(f"attribute (name):{person1.name}")
print(f"attribute (age):{person1.age}")
print(f"attribute (salary):{person1.salary}")
