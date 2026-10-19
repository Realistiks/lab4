print('Введите 3 стороны треугольника')
a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Равносторонний')
    elif a == b or b == c or a == c:
        print('Равнобедренный')
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        print('Прямоугольный')
    else:
        print('Разносторонний')
else:
    print('Такой треугольник не существует')