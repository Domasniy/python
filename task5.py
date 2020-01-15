income = int(input('Введите выручку фирмы: '))
expends = int(input('Введите издержки фирмы: '))

if income > expends:
    print('Фирма отработала с прибылью')
    rent = (income - expends) / income
    print(f'Рентабельность выручки {rent}')
    employees = int(input('Введите кол-во сотрудников в фирме: '))
    print(f'Один сотрудник принес {(income-expends)/employees} рублей прибыли')
elif income == expends:
    print('Фирма отработала в ноль')
else:
    print('Фирма отработала в убыток')