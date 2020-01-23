def int_func(word):
    return word.title()

#Вариант чтобы изменялась только первая буква слова

def int_func_capitalize(string):
    new_string = ''
    for word in string.split(' '):
        new_string += word[0].upper() + word[1:] + ' '
    return new_string

print(int_func('AbiRvalg DunaMja Kulan'))

print(int_func_capitalize('tesT kOlgbGGb fdGdfdfd dffDdffd'))