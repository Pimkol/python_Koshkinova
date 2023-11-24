def divide (a,b):
    if b==0:
        raise ZeroDivisionError ('Нельзя делить на 0')
    return a/b

print(' number 1')
a= int(input())
print(' number 2')
b= int(input())

print (divide(a,b))