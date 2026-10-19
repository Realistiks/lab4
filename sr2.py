print('Введите число для перевода')
try:
    chis = int(input())
    if chis >= 0:
        print(bin(chis)[2:])
        print(oct(chis)[2:])
        print(hex(chis)[2:])
    else:
        print('-' + bin(chis)[3:])
        print('-' + oct(chis)[3:])
        print('-' + hex(chis)[3:])
except ValueError:
    print('Введите целое число!!!')