#1

print ('введите оценку 1-10')
ocenka = int (input())
if (ocenka >0) and (ocenka <= 3):
    print ('Плохо')
elif (ocenka > 4) and (ocenka <=6):
    print ('Удовлетворительно')
elif (ocenka > 7) and (ocenka <= 9):
    print ('Хорошо')
else:
    print('Otlicno')

#2
print ('введите время')
vrem = int (input())
if (vrem>=6) and (vrem <= 12):
    print ('Доброе утро')
elif (vrem > 12) and (vrem <=18):
    print ('Добрый день')
elif (vrem > 18) and (vrem <= 24):
    print ('Добрый вечер')
else:
    print('Спокойной ночи')

# 3
print ('введите время')
num = int(input())
for i in range (1,num + 1):
    if i%3==0:
        print (f' делится на 3 ={i}')

#4
spisok= [1,2,3,-4,5,6,-7,8,-9,10]
count = 0
sum=0
for i in spisok:
    if i<0:
        continue
    else:
            count= count+1
            sum=sum+i
            a_v_g= sum/count
            print (a_v_g)
#5
visota = int(input("введите высоту елочки: "))
for i in range(visota):
    print(' ' * (visota - i - 1) + '*' * (2 * i + 1))
print(' ' * (visota - 1) + '*')

#6 с помощью подсказок google
for i in range(5):
    for j in range(i+1):
        print("*", end="")
    for j in range(8-2*i):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()

for i in range(4, -1, -1):
    for j in range(i+1):
        print("*", end="")
    for j in range(8-2*i):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()
# 7 пузырек
arr = [1,55,88,99,66]
for i in range(0, len(arr) - 1):
    for j in range(len(arr) - 1):
        if (arr[j] > arr[j + 1]):
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

    print(arr)
#8 

white = "██"
black = "  "
figura =  ' '

for i in range(8):
    for j in range(8):

        if (i + j) % 2 == 0:
            print(white, end="")
        else:
            print(black, end="")
    print()  
