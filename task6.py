current_km = float(input('Введите сколько километров пробежали в первый день: '))
finish_km = float(input('Введите на скольких километрах вы хотите остановиться: '))

day = 1
while current_km < finish_km:
    day = day + 1
    current_km = current_km + current_km / 10
print(day)