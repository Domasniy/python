user_string = input('Введите строку из нескольких слов с пробелами: ')
strings_list = user_string.split(' ')
for ind, word in enumerate(strings_list,1):
    print(f'{ind} - {word[:10]}')