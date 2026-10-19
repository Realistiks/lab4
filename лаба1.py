print('Введите число')
n = int(input())


print('Чётное' if n % 2 == 0 else 'Нечётное')
print('Делится на 3' if n % 3 == 0 else 'Не делится на 3')

if n > 0:
    print('Положительное')
elif n < 0:
    print('Отрицательное')
else:
    print('Ноль')