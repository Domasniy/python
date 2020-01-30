list_translate = ['Один', 'Два', 'Три', 'Четыре']
try:
    with open('number.txt') as file_r:
        for line in file_r:
            try:
                with open('number_translate.txt','a+',encoding='utf-8') as file_res:
                    file_res.write(list_translate.pop(0) + ' - ' + line.split('-')[1].lstrip())
            except:
                print('что-то пошло не так')
except IOError:
    print('Ошибка чтения файла. Проверьте название файла')