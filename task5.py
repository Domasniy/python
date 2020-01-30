from random import randint

try:
    with open('nums.txt','w+') as file_w:
        file_w.write(' '.join(str(randint(1,100)) for i in range(5)))
        file_w.seek(0)
        numbers = file_w.read()
        print(f'Числа: {numbers}\nСумма: {sum(int(num) for num in numbers.split())}')
except IOError:
    print('Ошибка записи в файл')
