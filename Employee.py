class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and my salary is {self.salary}")


p = Person("Ali", 26)

e = Employee("Maria", 21, 50000)
e.show()
