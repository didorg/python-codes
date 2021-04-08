class Person:
    __height = None
    __weight = None

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

    def speak(self):
        print(f'{self.name} is speaking')

    def __repr__(self):
        return self.name + " " + self.last_name + " " + str(self.age)
