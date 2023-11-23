class Animal(ABC):
    @abstractmethod
    def Proverka(self):
        pass
class Flyable(ABC):
    @abstractmethod
    def Info(self):
        pass
class Proiz(Animal,Flyable):
        def Proverka(self):
             print ('Это метод первого класса')
        def Info(self):
             print ('Это метод 2 класса')
proba= Proiz()
proba.Proverka() 
#3 
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def Proverka(self):
        pass

class Vehicle(ABC):
    @abstractmethod
    def __init__(self, model, year):
        self.model=model
        self.year=year  
    def Info():
        print ('Это базовый класс')

class Car(Vehicle):
    def __init__(self, model,year,fuel_type):
        super().__init__(model,year)
        self.fuel_type=fuel_type

class Toyota(Car):
    def __init__(self, model,year,fuel_type, model_name, fuel_efficciency):
        super().__init__(model,year,fuel_type)
        self.model_name=model_name
        self.fuel_efficciency=fuel_efficciency
    def Info():
        print ('Это Тайота')
class Tesla(Car):
    def __init__(self, model,year,fuel_type, model_name, fuel_efficciency):
        super().__init__(model,year,fuel_type, model_name, fuel_efficciency)
    def Info():
        print ('Это Tesla')    
cariki = Car()
