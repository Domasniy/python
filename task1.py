class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        return f'Матрица {len(self.matrix_list)} на {len(matrix_list[0])}\n\n' + '\n\n'.join([''.join([f'{num:5}' for num in row]) for row in self.matrix_list]) + '\n'
    
    def __add__(self,other):
        try:
            if len(self.matrix_list) == len(other.matrix_list) and len(self.matrix_list[0]) == len(other.matrix_list[0]):
                return Matrix([[other.matrix_list[ind][indrow] + num for indrow,num in enumerate(row)] for ind, row in enumerate(self.matrix_list)])
            else:
                raise ValueError
        except ValueError:
            print('Ошибка сложения матриц!\nМатрицы должны быть одной размерности!')


matrix_list = [[3, 5, 8], [8, 3, 1],[4, 2, 3]]
matrix_list2 = [[10, 15, 9], [-8, 5, 1],[32, 52, 12]]
m = Matrix(matrix_list)
m2 = Matrix(matrix_list2)
print(m)
print(m2)
print(f'Результат сложение двух матриц\n {m + m2}')