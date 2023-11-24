from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Drawable):
    def __init__(self, radius):
        self.radius = radius
    
    def draw(self):
        print(f"Рисую круг с радиусом {self.radius}")

class Rectangle(Drawable):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def draw(self):
        print(f"Рисую прямоугольник с размерами {self.w}x{self.h}")

shapiki = [Circle(6),Rectangle(3,8)]
for sh in shapiki:
    print (sh.draw())
