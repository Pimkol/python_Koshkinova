class IntMag():
    def __init__(self ):
        # self.tov_name=tov_name,
        # self.descr=descr, 
        # self.price = price
        self.tovar = []

    def Add_info (self,tov_name,descr, price):
        tovar_n = {
            'tov_name':tov_name,
            'descr':descr,
            'price':price
        }
        self.tovar.append(tovar_n)

    def show_descr(self, tov_name):
        for i in self.tovar:
            if (i['descr']== tov_name):
                print(i['descr'])
                print(i['price'])
            else:
                print ('Такого товара нет')

    def pomen_price(self, tov_name, price_new ):
        self.price = self.price + price_new
        return self.price

        

mag= IntMag()
print ('Добавьте пожалуйста товар в магазин')
name= input()
print ('Добавьте пожалуйста описание товара')
description = input()
print ('Добавьте пожалуйста цену')
price_n = int (input())
mag.Add_info(name, description, price_n)

print ('Описание какого товара нужно найти?')
opisanie= input()
mag.show_descr(opisanie)
print ('На какой товар поменять цену')
name_t= input()
print ('Введите новую цену')
pr= int(input())
mag.pomen_price (name_t,pr)