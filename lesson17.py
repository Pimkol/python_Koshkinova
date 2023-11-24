def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y


#2
from abc import ABC, abstractmethod
class Shape (ABC):
    def __init__(self):
        pass

    @abstractmethod
    def Area():
        pass

class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def Area(self):
        return f'S = {3.14 *self.r*self.r}'
    
class Treangle(Shape):
    def __init__(self,a,h):
        self.a= a
        self.h=h
    def Area(self):
        return 1/2* (self.a*self.h)
    
class Rectangle(Shape):
    def __init__(self,st1,st2):
        self.st1=st1
        self.st2=st2
    def Area(self):
        return self.st1*self.st2
    
shapiki = [Circle(6),Treangle(4,5),Rectangle(3,8)]
for sh in shapiki:
    print (sh.Area())

#3
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
