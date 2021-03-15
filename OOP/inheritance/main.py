from rectangle import Rectangle
from triangle import Triangle
from loguru import logger

rect = Rectangle()
tri = Triangle()

rect.set_values(50, 30)
rect.set_color('blue')

tri.set_values(30, 40)
tri.set_color('red')

print(f'Rectangle area is {rect.area()} and color is {rect.get_color()}')

print(f'Triangle area is {tri.area()} and color is {tri.get_color()}')
logger.info("This is the info logger")

