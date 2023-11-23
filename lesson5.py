# Задание 1
num = int (input('Введите число '))
for i in range (num+1):
    if i%2==0:
        print (i)

# Задание 2
sum=0
num = int (input('Введите число '))
for i in range (num+1):
    sum = sum+i
print (f'Сумма всех чисел от 0 до {num} = {sum}')

# Задание 3
for i in 'python':
    print(i)

# Задание 4
sum = 0
i=0
while i<100:
    if i%2!=0:
        a= sum=sum+i
    i=i+1
print (a)

# Задание 5
for i in range(21):
    if (i%2==0):
        print (i)

#Задание 6
num = int(input())
for i in range (11):
    print (i*num)

#Задание 7 таблица умножения
num = int(input('Введите число '))
for i in range (11):
    print (f' {i} * {num} = {i*num}')

#Задание 8 Елочка
for i in range (6):
    for j in range (6):
        print (j*'*')

#Задание 9 Таблица умножения с вложенными циклами
for i in range (1,6):
    for j in range (1,6):
        print (f'{i} *{j} = {i*j}')
    print ('\n')

#Задание 10 Простое число ч/з вложенный цикл (нужна доработка)
print ('Введите число')
n= int (input())
for i in range (1,n):
    for j in range (1,i):
        if (i/i ==1) and (i/1 ==i):
            print (i)

#Задание 11
print ('введите число  ')
num1= int (input())
for i in range(num1):
    if (i%2==0):
        print (i)

#Задание 12
for i in range (1):
    print ('Сколько месяцев в году?')
    ans= int(input())
    if ans==12:
        print ('Правильно')
    else:
        print ('Не правильно')
    
    print ('Продолжаем? если Да нажмите +, если нет нажмите -')
    symbol=input()
    if symbol=='+':
        print ('Сколько дней в неделе?')
        ans= int(input())
        if ans==7:
            print ('Правильно')
        else:
            print ('Не правильно')
    else:
        break
    print ('Продолжаем? если Да нажмите +, если нет нажмите -')
    symbol=input()
    if symbol=='+':
        print ('Сколько дней в январе?')
        ans= int(input())
        if ans==31:
            print ('Правильно')
        else:
            print ('Не правильно')
    else:
        break
    print ('Продолжаем? если Да нажмите +, если нет нажмите -')
    symbol=input()
    if symbol=='+':
        print ('Сколько дней в сентябре?')
        ans= int(input())
        if ans==30:
            print ('Правильно')
        else:
            print ('Не правильно')
    else:
        break

# Задание 12
import random
rand= random.randint(0,10)
print('Введите число')
number = int (input())
while True:
    
    if (number == rand):
        print ('ПОБЕДА')
    elif (number <rand):
        print ('Ваше число меньше')
    else:
        print ('Ваше число больше')
    print ('Хотите продолжить? Да или Нет')
    answer = input()
    if answer == 'да':
        print('Введите число')
        number = int (input())
    else:
        print ('Спасибо за игру')
        break


