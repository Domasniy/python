try:
    with open('test.txt') as f:
        content = f.readlines()
        print(f'В файле содержится {len(content)} строк')
        for index, stroka in enumerate(content, 1):
            print(f'В {index} строке содержится {len(stroka.split())} слов')
        f.seek(0)
        content_all = f.read()
        char_count = len(content_all)-content_all.count("\n")
        print(f'В файле содержится {char_count} символов, исключая переходы на новые строки')
except IOError:
    print('Ошибка чтения файла, проверьте что указано верное файла')    