number = int(input('Введите целое, положительное число: '))
original_num = number
if number // 10 == 0:
    max_num = number
else:
    max_num = 0
    while (number // 10) != 0:
        if (number % 10) > max_num:
            max_num = number % 10
        number = number // 10
        
    if (number % 10) > max_num:
        max_num = number % 10

print (f'Самая большая цифра в числе {original_num} это {max_num}')