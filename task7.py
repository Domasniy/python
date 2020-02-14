class ComplexNumber():

    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def __str__(self):
        return f'Комплексное число {self.i} + {self.j}i'
    
    def __add__(self, other):
        return ComplexNumber(self.i + other.i, self.j + other.j)
    
    def __mul__(self, other):
        return f'{(self.i * other.i - self.j * other.j)} + {(self.i * other.j + self.j * other.i)}i'


num1 = ComplexNumber(4, 8)
num2 = ComplexNumber(5, 9)

print(num1)
print(num2)
print(f'Сумма равна {num1 + num2}')
print(f'Сумма равна {num1 * num2}')