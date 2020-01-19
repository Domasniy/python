user_month = int(input('Введите номер месяца: '))

dict_year_period = {'Зима': [12, 1, 2], 'Весна': [3,4,5], 'Лето': [6,7,8], 'Осень':[9,10,11]}

for key, value in dict_year_period.items():
    for val in value:
        if val == user_month:
            print(f'Этом месяц относиться к времени года {key}')
            break