#1
def Pl(a,h):
    S = (a * h) / 2
    return S
print (Pl(10,15))

#2
import math
r=int(input('Radius = '))
S= math.pi*math.pow(r,2)
print (f'Ploshad = {S:.2f}')

#3
import datetime
date1 = datetime.datetime.today() + datetime.timedelta(days=7)
print(date1)

#4
def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
print (is_prime(3))   

#5
import datetime
st_d= datetime.datetime(2023,11,6,10,0,0)
st_d2= datetime.datetime(2023,11,15,10,0,0)
raznica= st_d2-st_d
print (raznica)

#6
import random 
letter = ['a','b','c','d','e', 1, 2,3,4,8]
for i in range (5):
    random_name = random.choice(letter)
    print (random_name,end='')

#7
import datetime
date = datetime.datetime(2023, 11, 6)
print(date.weekday())

#8
import random 
uchastniki = ['Кошкинова', 'Жакенов','Алиханов','Алиханова']
for i in range (len(uchastniki)):
    random.shuffle(uchastniki)
    print(uchastniki[i])
    break
#9 С помощью подсказок google
import datetime
import time
start_time = datetime.datetime.now()
for i in range (datetime.timedelta(minutes=1)):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)
    time.sleep(1)
start_time = datetime.datetime.now()
while datetime.datetime.now() - start_time < datetime.timedelta(minutes=1):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)
    time.sleep(1)

#10
import datetime
import time
current_time = datetime.datetime.now().strftime("%H:%M:%S")
print (current_time)  

#11
import datetime
import time
import random
h=random.randint(0,12)
m=random.randint(0,60)
s=random.randint(0,60)
c_date= datetime.time(h,m,s)
f_date= c_date.strftime("%H:%M:%S")
print (f_date)