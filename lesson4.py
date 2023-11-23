a= int(input('Введите 1 число'))
b= int(input('Введите 2 число'))
if a>b:
    print (f'большее {a}')
elif a==b:
    print ('Одинаковые')
else:
    print (f'большее {b}')

#задание 2

a= int(input('Введите число'))
if a>=10 and a<=10:
    print (f' {a}Число лежит в диапазоне от 10 до 20')
else:
    print (' Не лежит')

#задание 2
print ('Введите Ваш возраст')
age= int(input())
if age>=18:
    print ('Вы можете управлять авто')
else:
    print ('Не можете')

# Практическое задание для самостоятельной работы 1
ocenka=int(input('Какую оценку ты сегодня получил?'))
if ocenka==5:
    print ('Отлично')
elif ocenka==4:
    print ('Хорошо')
elif ocenka==3:
    print ('Удовлетворительно')
elif ocenka==2:
    print ('Не удовлетворительно')
else:
    print ('Такой оценки не бывает')

# Практическое задание для самостоятельной работы 2
age = int(input('Введите возраст '))
if 2>age>0:
    print ('Младенец')
elif 2<age<12:
    print ('Ребенок')  
elif 12<age<18:
    print ('Подросток')   
elif 18<age<35:
    print ('Молодежь')
elif 35<age<60:
    print ('Взрослый')    
else:
    print ('Пожилой')

#задание для практики 1 уже выполнено выше, второе ниже:
x= int (input('Введите координату х'))
y=int (input('Введите координату у'))
if (x>0) and (y>0):
    print ('Первая четверть')
elif (x<0) and (y>0):
    print ('Вторая четверть')
elif (x<0) and (y<0):
    print ('Третья четверть')
else:
    print ('Четвертая четверть')

#задание для практики 3-1
a= int(input('Введите число; '))
if a%2==0:
    if a%4==0:
        print ('Четное и делится на 4')
    else:
        print ('Четное, но на 4 не делится')
else:
    print ('Нечетное')

# Практика 3, задание 2
oc=int(input('Какую оценку ты сегодня получил?  Варианты : от 10 до 1'))
if (oc==10) or (oc==9) :
    print ('Отлично')
elif (oc==8) or (oc==7):
    print ('Хорошо')
elif (oc==6) or (oc==5):
    print ('Удовлетворительно')
elif (oc==5) or (oc==4):
    print ('Не удовлетворительно')
else:
    print ('У Вас есть дополнительные задания?')
# Практика 4, задание 1

print ('Введите число')
num = int(input())
if (num>0) and (num%2==0):
    print ('Число четное и положительноe')
else:
    print ('Нечетное')

# Практика 4, задание 2
print ('Введите год')
god= int(input())
if (god%4==0)and (god%100!=0) or (god%400==0):
    print ('Высокосный')
else:
    print ('нет')

# Практика 4, задание 3
age= int (input('Введите возраст'))
med_zakl=input('Имеются ли у Вас серьезные медецинские ограничения')

if med_zakl=='нет':
    if (age>18) and (age<45):
        print ('Может пройти на матч')
    else:
        print ('Не может, не подходит по возрасту')
else:
    print ('Не может, есть медецинские противопоказания')

# Практика 5, задание 1
print ('Сколько месяцев в году? Выберите правильный варианt')
print ('1- 12 \n2- 15\n3- 14 \n')
print ('Введите вариант ответа 1, 2 или 3')
otvet= int(input())

if otvet == 1:
    print ("Правильно")
elif (otvet == 2) or (otvet==3) :
    print ("Не Правильно")
print ('Сколько дней в неделе? Выберите правильный варианt')
print ('1- 7 \n2- 8\n3- 9 \n')
print ('Введите вариант ответа 1, 2 или 3')
otvet= int(input())

if otvet == 1:
    print ("Правильно")
elif (otvet == 2) or (otvet==3) :
    print ("Не Правильно")

# Практика 5, задание 2

login = 'nazik@gmail.com'
password=1234

log=input('Введите логин ')
pas_w= int(input('введите пароль '))

if (log==login) and (pas_w==password):
    print ('Введенные данные верны')
else:
    print ('Не верные логин или пароль')


# Практика 5, задание 3
ves=int(input('Введите вес товара'))
st_ves= (int(input('введите стоимость за 1 кг товара')))
rast=int(input('Введите  расстояние'))
st_ras= (int(input('введите стоимость за 1 км')))

dostavka = ves*st_ves+ rast*st_ras
print (f'Стоимость доставки = {dostavka}')