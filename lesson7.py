#1 Перевести температуру  F, C
def Konvert (Cels,Far):
    f= (Cels*(9/5)+32)
    c=5/9*(Far-32)
    return f,c
print (Konvert (20,40))

#2 НОК
def NOD(a, b):
    while b:
        a, b = b, a % b
    return a
def NOK(a, b):
    return (a * b) // NOD(a, b)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
result = NOK(num1, num2)
print("НОК:", result)

#3 Не поняла условие, сделала примерно
def Calc(ipoteka, avto, zp):
    
    ostatok = zp-ipoteka-avto
    return ostatok

ip =int (input('ipoteka = '))
av =int (input ('avto = '))
print (Calc(ip,av, 2000000))

#4 Палиндром из цифр
def is_palindrome_number(number):
    str_number=str(number)
    map_fun=map(int,str_number)
    perevod_spisok=list(map_fun)
    if perevod_spisok==perevod_spisok[::-1]:
        otvet = 'Да'
    else: otvet='Нет'
    return otvet
        
print (is_palindrome_number(12323))   