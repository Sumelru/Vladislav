import math
def c(a, b):
    c=math.sqrt(a**2+b**2)
    return c
a=int(input('Введите катет 1 треугольника: '))
b=int(input('Введите катет 1 треугольника: '))
a1=int(input('Введите катет 2 треугольника: '))
b1=int(input('Введите катет 2 треугольника: '))
if c(a, b)>c(a1, b1):
    print('Гипотенуза 1 треугольника больше')
elif c(a, b)<c(a1, b1):
    print('Гипотенуза 2 треугольника больше')
else:
    print('Гипотенузы равны')