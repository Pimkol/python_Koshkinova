#1
lists =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in lists:
    for elem in row:
        print (elem, end= ' ')
    print ()

#2
zhanr ={
    "musik":{
        "Название":'Hello World'
    },
    "kino":{
        "Название":'Hello Bob'
    }
}
for i in zhanr:
    print('Введите жанр musik или kino')
    c= input()
    print('Введите название')
    s= input()
    zhanr[c]['название']=s
    break
print (zhanr)

#3

# students ={
#     "Кошкинова":{
#         "предмет":"математика", 'оценка':5,
#         "предмет":"информатика", 'оценка':5,
#         "предмет":"физика", 'оценка':5,
#     },
#     "Жакенов":{
#         "предмет":"математика", 'оценка':3,
#         "предмет":"информатика", 'оценка':3,
#         "предмет":"физика", 'оценка':3,
#     },
#     "Алиханов":{
#         "предмет":"математика", 'оценка':4,
#         "предмет":"информатика", 'оценка':4,
#         "предмет":"физика", 'оценка':3,
#     }


# }

# def Avg(fio):
#     sum = 0
#     count=0
#     for student, ocenki in students.items():
#         value=ocenki['оценка']
#         sum = sum+value
#         count= count+1
#         avg_n= sum/count
#     return avg_n
    
# print (Avg('Жакенов'))

students = {
    "Студент1": [4, 5, 3, 4],
    "Студент2": [5, 4, 4, 5],
    "Студент3": [3, 3, 4, 4]
}

def Srr_ocenka(students):
    for st, ocenka in students.items():
        sr_oc = sum(ocenka) / len(ocenka)
        print(f"Средняя оценка студента {st}: {sr_oc}")

print (Srr_ocenka(students))


#5
coordin = (1,2,3)
sum=0
for i in range (len(coordin)):
    sum = sum+coordin[i]
print (sum)

'''А как сделать с таким кортежем?
coordin = ((1,2,3),(1,6,3),(1,8,9))
sum=0
# for row in coordin:
#     for elem in row:
#         print (elem,end=" ")
#     print ()

for i in range (len(coordin)):
    for j in i:
        sum = sum+coordin[j]
print (sum)
'''