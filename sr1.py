import random

chislo = random.randint(1, 100)
tries = 0

print('Угадай число) От 1 до 100')

while True:
    try:
        guess = int(input('Твой вариант: '))
    except ValueError:
        print('Введите число!')
        continue

    if guess < chislo:
        print("Больше")
        tries += 1
    elif guess > chislo:
        print("Меньше")
        tries += 1
    else:
        print(f'Угадали! За {tries} попыток')
        break