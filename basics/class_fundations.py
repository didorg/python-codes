class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'{self.name} is speaking')

    def walk(self):
        print(f'{self.name} is walking')


john = Person('John', 25)
john.speak()
john.walk()
