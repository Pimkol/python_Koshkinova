#2
sotrudniki = ('Кошкинова','Жакенов','Усович')
for sotr in sotrudniki:
    print (sotr)

#3
spisok = [1,5,6,9,8,11,78,55]
print (spisok)
print ('какое число удалить из списка')
a= int( input())
spisok.remove(a)
print(spisok)

#4
fruits= ['apple', 'avocado', 'apricot','banana','kok']
fruits2=[]
for i in range (len(fruits)):
    if len(fruits[i])<5:
        fruits2.append(fruits[i])
print (fruits2)

#4-------?
fruits= ['apple', 'avocado', 'apricot','banana','kok']
for i in range (len(fruits)):
    if len(fruits[i])>5:
        fruits.remove(fruits[i])
print (fruits)

#5
students=[('Alisher', 90),('Alex', 80)]
for inf in students:
    print (inf)

#6
number =[]
for i in range (0,21):
    if i%2==0:
        number.append(i)
print (number)

#7
number =[]
summ= 0
for i in range (0,21):
    number.append(i)
    s= number[i]**2
    summ= summ+s
print (summ)

#8
row = int(input("Количество столбцов:"))  
column = int(input("Количество строк:"))  
matrix = []  
print("Введите элеметы матрицы:")  
  
for i in range(row):       
   a =[]  
   for j in range(column):     
      a.append(int(input()))  
   matrix.append(a)  
 
for i in range(row):  
   for j in range(column):  
      print(matrix[i][j], end = " ")  
   print()  