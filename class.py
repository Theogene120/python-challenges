class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f"Hello {self.name} I'm {self.age} years old " )
    
p1 = Person('Theo', 22)

p1.greeting()
