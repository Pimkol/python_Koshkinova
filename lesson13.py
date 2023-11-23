#2 
class Person():
    def __init__ (self, name,age):
        self.name = name
        self.age = age
    def get_info(self):
        return f' Фамилия:{self.name}  Возраст:{self.age}'
    
class Employee(Person):
    def __init_(self, name,age,salary):
        super().__init__(name, age)
        self.salary = salary
    def get_info(self):
        return f' Фамилия:{self.name}  Возраст:{self.age} зарплата:{self.salary}'

person1 = Person('Кошкинова', 25)
emp1 = Employee('Кошкинова',25,3500)
print (person1.get_info())
print (emp1.get_info())

#3
class Animals():
   def speak(self):
      print ('')

class Cat(Animals):
   def speak(self):
      print ('Мяу')

class Dog(Animals):
   def speak(self):
      print ('Гав')
dog= Dog()
dog.speak()
cat= Cat()
cat.speak()

#4
class BankAccount():
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    
    def deposit(self, summ_vklada):
        self.balance += summ_vklada
        
    def withdraw(self, summ_snatia):
        if self.balance >= summ_snatia:
            self.balance -= summ_snatia
        else:
            print("Недостаточно средств")

class SavingsAccount(BankAccount):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        self.balance += self.balance * self.interest_rate

account = BankAccount(1000, "1234567890")
account.deposit(500)
account.withdraw(200)
print(account.balance)  
print(account.account_number)  