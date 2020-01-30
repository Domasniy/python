try:
    with open('workers.txt',encoding='utf-8') as f:
        salary_sum = 0
        workers_count = 0
        print('Сотрудники с зарплатой менее 20000 рублей')
        print(f'{"Cотрудник":>15} | {"Зарплата":>15}')
        print('-------------------------------------')
        for line in f:
            salary = float(line.split()[1].rstrip('\n'))
            salary_sum += salary
            workers_count += 1
            if salary < 20000:
                print(f'{line.split()[0]:>15} | {salary:>15}')
        print(f'Средняя величина доходов сотрудников: {salary_sum/workers_count:.2f} рублей')
except IOError:
    print('Ошибка чтения. Проверьте имя файла.')