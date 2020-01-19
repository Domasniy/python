products = [(0, {'название': 'Компьютер', 'цена': 4000, 'количество': 2, 'eд': 'шт'}), (1, {'название': 'Монитор', 'цена': 2000, 'количество': 7, 'eд': 'шт'})]
count = len(products)
while True:
    print('*'*50)
    print(f'Кол-во товаров в базе: {count}')
    command_select = input('Выберете действие:\n1 - Добавить товар\n2 - Ввывести список товаров в базе\n3 - Ввывести аналитику\n4 - Выход\n')
    if command_select == '4':
        print('Cпасибо за использование программы. До встречи')
        break
    elif command_select == '1':
        prod_dict = {}
        prod_dict['название'] = input('Введите название товара: ')
        prod_dict['цена'] = int(input('Введите цену: '))
        prod_dict['количество'] = int(input('Введите кол-во: '))
        prod_dict['eд'] = 'шт'
        products.append((count,prod_dict))
        count += 1
    elif command_select == '2':
        for product in products:
            print(product)
    elif command_select == '3':
        prod_analyze = {'название': [], 'цена': [], 'количество': [], 'ед': 'шт'}
        for prod in products:
            prod_analyze['название'].append(prod[1]['название'])
            prod_analyze['цена'].append(prod[1]['цена'])
            prod_analyze['количество'].append(prod[1]['количество'])
        for key, value in prod_analyze.items():
            print(f'{key} - {value}')
    else:
        print('Пожалуйста выберете правильное действие из списка!')
        continue