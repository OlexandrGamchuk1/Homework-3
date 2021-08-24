a = int(input('Enter the number a '))
b = int(input('Enter the number b '))
c = int(input('Enter the number c '))
if b < a > c:
    print('Maximal a')
elif a < b > c:
    print('Maximal b')
elif a < c > b:
    print('Maximal c')
else:
    print('There is no maximum')