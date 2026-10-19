print('Введите возраст')
age = int(input())

if age < 0:
    print('Ошибка: возраст не может быть отрицательным')
elif age <= 12:
    print('Ребёнок')
elif age <= 17:
    print('Подросток')
elif age <= 64:
    print('Взрослый')
else:
    print('Пожилой')