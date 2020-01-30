with open('user_text.txt','w') as f:
    while True:
        user_string = input('Вводите строки, для окончания ввода введите пустую строку: ')
        if user_string:
            f.write(user_string+'\n')
        else:
            break
