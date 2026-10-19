print('Введите вес (кг) и рост (м)')
try:
    ves = float(input())
    rost = float(input())

    if ves <= 0 or rost <= 0:
        print('Введите положительные числа!')
    else:
        imt = ves / (rost ** 2)
        if imt < 18.5:
            kat = 'недостаточный вес'
        elif imt < 25:
            kat = 'норма'
        elif imt < 30:
            kat = 'избыточный вес'
        else:
            kat = 'ожирение'
        print(f'ИМТ = {imt:.1f}, категория: {kat}')
except ValueError:
    print('Введите числа!')