def two_num_division(num1, num2):
    return num1 / num2

while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print(f'{num1} / {num2} равняется {two_num_division(num1, num2)}')
        break
    except ZeroDivisionError:
        print ('На ноль делить нельзя')
    except ValueError:
        print ('Можно вводить только числа')
