class OwnAddError(Exception):
    def __init__(self,txt):
        self.txt = txt

result_list = []

while True:
    user_input = input('Введите число или слово stop, чтобы выйти: ')
    if user_input.lower() == 'stop':
        print(f'Получился следующий список чисел: {result_list}')
        break
    try:
        if not user_input.isdigit():
            raise OwnAddError("Ввводить можно только цифры")
        result_list.append(user_input)
    except OwnAddError as err:
        print(err)
