print('Введите номер месяца и год')
month = int(input('Месяц (1-12): '))
year = int(input('Год: '))

if month < 1 or month > 12:
    print('Нет такого месяца')
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('29 дней')
    else:
        print('28 дней')
elif month in (4, 6, 9, 11):
    print('30 дней')
else:
    print('31 день')