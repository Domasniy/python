sum = 0
exit_status = False
while True:
    user_input = input('Вводите числа разделенные пробелами. Для завершения введите "q"\n: ')
    if user_input.lower() == 'q' and len(user_input) == 1:
        print("До встречи")
        break
    input_list = user_input.split(' ')
    for num in input_list:
        try:
            sum += int(num)
        except ValueError:
            print (f'Сумма введенных чисел: {sum}\n До встречи')
            exit_status = True
            break
    if exit_status:
        break
    print(f'Сумма введенных чисел: {sum}')
            
        

