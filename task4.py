# Вариант 1. С использованием **
def num_power(x, y):
    if x < 0:
        raise ValueError('Первое число должно быть положительным') 
    if y>0 or not isinstance(y, int):
        raise ValueError('Второе число должно быть целым отрицательным')  
    print(x ** y)

# Вариант 2. Без использования **
def num_power_second(x,y):
    if x < 0:
        raise ValueError('Первое число должно быть положительным') 
    if y>0 or not isinstance(y, int):
        raise ValueError('Второе число должно быть целым отрицательным')  
    count = 0
    result = 1
    while count < abs(y):
        result /= x
        count += 1   
    print(result)

num_power(10, -3)
num_power_second(10, -3)

