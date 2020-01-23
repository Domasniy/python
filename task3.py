def sum_of_two_biggest(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers.remove(min(numbers))
    return sum(numbers)

print(f'Сумма наибольших двух аргументов равна {sum_of_two_biggest(5,2,3)}')