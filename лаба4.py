import math

print('Введите коэффициенты a, b, c')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a == 0:
    print('Это не квадратное уравнение')
else:
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f'Два корня: x1 = {x1:.2f}, x2 = {x2:.2f}')
    elif d == 0:
        print(f'Один корень: x = {-b / (2 * a):.2f}')
    else:
        print('Нет действительных корней')