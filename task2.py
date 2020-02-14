class OwnZeroError(Exception):
    def __init__(self,txt):
        self.txt = txt

num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
try:
    if int(num2) == 0:
        raise OwnZeroError("На ноль делить нельзя")
    result = int(num1) / int(num2)

except ValueError:
    print("Вы ввели не число")
except OwnZeroError as err:
    print(err)
else:
    print(f"Все хорошо. Результат деления: {result}")