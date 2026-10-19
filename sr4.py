print('Введите координаты точки')
x = float(input('x = '))
y = float(input('y = '))

if x == 0 and y == 0:
    print('Точка в начале координат')
elif x == 0:
    print('Точка на оси Y')
elif y == 0:
    print('Точка на оси X')
elif x > 0 and y > 0:
    print('I четверть')
elif x < 0 and y > 0:
    print('II четверть')
elif x < 0 and y < 0:
    print('III четверть')
else:
    print('IV четверть')