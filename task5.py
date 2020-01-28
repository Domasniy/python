from functools import reduce

print(reduce(lambda prev_el, el: prev_el * el, [el for el in range(100,1001) if el % 2 == 0]))