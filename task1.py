from sys import argv
try:
    time, rate, bonus = argv[1:]
except ValueError:
    print(f'Скрипт принимает строго 3 аргумента : часы, ставка, бонус \nВы ввели {len(argv)-1} аргумент(а)')
else:
    try:
        salary = (int(time) * int(rate)) + int(bonus)
        print(f'Сотрудник отработал {time} часов по ставке {rate} рублей в час, плюс он получил премию {bonus}.\nЗарплата сотрудника: {salary}')
    except ValueError:
        print('Скрипт принимает только числа, введите 3 аргумента : часы, ставка, бонус')