class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def myfunc(self):
        print(f"Hello my name is {self.name}, Im {self.age} years old and i living {self.address} ")
# Example usage
p1 = Person("Esmanur", 20, "Poland")
p1.myfunc()
