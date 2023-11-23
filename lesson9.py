'''student = {'Koshkinova':5, 'Zhakenov':2, 'Alihanov':4}
for key, value in student.items():
    print (key,':', value)

for key, value in student.items():
    if value==2:
       del student[key]
       break
# for key in student.keys():
#     if key=='Koshkinova':
#        del student[key]
#        break
print ('******************')
for key, value in student.items():
      print (key,':', value)'''
 
 #2
A = {1, 2, 3, 4, 5}
B = {6, 2, 7, 4, 8}
print (A.intersection(B))
print (A.union(B))

#3
Strani = {
    'Kazakhstan':'Astana',
    'Russia': 'Moscow', 
    'USA': 'Washington'}
print('Введите страну')
c= input()
print('Введите столицу')
s= input()
Strani[c]= s
print (Strani)

#4
inventory = {
1: {'название': 'молоток', 'количество': 10, 'цена': 50},
2: {'название': 'гвозди', 'количество': 20, 'цена': 30},
3: {'название': 'лопата', 'количество': 15, 'цена': 80}
}

#5
inventory = {
1: {'название': 'молоток', 'количество': 10, 'цена': 50},
2: {'название': 'гвозди', 'количество': 20, 'цена': 30},
3: {'название': 'лопата', 'количество': 15, 'цена': 80}
}
    
def Search (A,key_tov):
    value = A[key_tov]
    return value
print ('Введите идентификационный номер')
number= int(input())
print (Search(inventory,number))

#6
inventory = {
1: {'название': 'молоток', 'количество': 10, 'цена': 10},
2: {'название': 'гвозди', 'количество': 20, 'цена': 30},
3: {'название': 'лопата', 'количество': 15, 'цена': 80}
}
def Summ (A):
   sum=0
   for i in inventory.values():
        value = i['цена']
        sum = sum+value
   return sum
print (Summ(inventory))

#7 
A = {1, 2, 3, 4, 5}
B = {6, 2, 7, 4, 8}

#8 
A = {1, 2, 3, 4, 5}
B = {6, 2, 7, 4, 8}

def Peresechenie(A,B):
    return A.intersection(B)
print (Peresechenie(A,B))

#9
A = {1, 2, 3, 4, 5}
B = {6, 2, 7, 4, 8}

def Peresechenie(A,B):
    return A.union(B)
print (Peresechenie(A,B))

