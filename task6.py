summary_dict = {}
try:
    with open('lessons.txt',encoding='utf-8') as f:
        for line in f:
            lesson = line.split()[0][:-1]
            time = 0
            for string in line.split()[1:]:
                if string == '-':
                    continue
                else:
                    time += int(string.split('(')[0])
            summary_dict[lesson] = time
        print(summary_dict)
except IOError:
    print('Ошибка чтения файла')