print('Введите 2 числа')
a = float(input())
b = float(input())
operation = input('Операция (+, -, *, /): ')

match operation:
    case '+':
        print(a + b)
    case '-':
        print(a - b)
    case '*':
        print(a * b)
    case '/':
        if b == 0:
            print('На ноль делить нельзя!')
        else:
            print(a / b)
    case _:
        print('Неизвестная операция')