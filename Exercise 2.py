a = int(input('Enter the side of the triangle '))
b = int(input('Enter the side of the triangle '))
c = int(input('Enter the side of the triangle '))
if a + b > c or a + c > b or c + b > a:
    print('The triangle exists')
else:
    print('No triangle')