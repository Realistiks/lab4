print('Введите 3 числа')
a = float(input())
b = float(input())
c = float(input())

max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c

print('Максимум:', max_num)