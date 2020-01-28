from sys import argv
from itertools import count,cycle

if argv[1] == 'count':
    try:
        num_start = int(input('Введите начальную цифру отсчета: '))
        num_end = int(input('Введите конечную цифру отсчета: '))
    except ValueError:
        print('Можно вводить только числа')
    else:
        for el in count(num_start):
            if el > num_end:
                break
            else:
                print(el)
elif argv[1] == 'cycle':
    user_list = input('Введите элементы списка через пробел: ').split()
    try:
        cycle_num = int(input('Введите сколько элементов вы хотите выввести в лупе: '))
    except ValueError:
        print('Можно вводить только числа')
    else:
        сount = 0
        for el in cycle(user_list):
            if сount >= cycle_num:
                break
            print(el)
            сount += 1
else:
    print('Можно использовать только след. опции для скрипта:\ncount - для вывода цифр от начального числа до конечного\ncycle - для вывода нужного кол-ва элементов списка по кругу')



