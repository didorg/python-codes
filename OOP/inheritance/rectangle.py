from polygon import Polygon
from shape import Shape


class Rectangle(Polygon, Shape):
    def area(self):
        return self.get_width() * self.get_height()
