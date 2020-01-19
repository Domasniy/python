original_list = []

while True:
    print(f'Текущий список: {original_list}')
    user_input = input('Введите элемент для добавления в список.\nДля окончания добавления элементов введите "end"\n: ')
    if user_input.lower() == 'end':
        break
    else:
        original_list.append(user_input)


result_list = []

for index, el in enumerate(original_list):
    if index + 1 == len(original_list) and len(original_list) % 2 != 0: 
        result_list.append(original_list[index])
        continue
    result_list.append(original_list[index+1]) if index % 2 == 0 else result_list.append(original_list[index-1])

print('*'*70)
print(f'{"Оригинальный список:":<40} {original_list}')
print(f'{"Список после обмена соседних элементов:":<40} {result_list}')     
