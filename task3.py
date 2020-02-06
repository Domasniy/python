class OrganicCell:

    def __init__(self, cells):
        self.cells = cells
    
    def __str__(self):
        return f'Клетка содержит {self.cells} ячеек'
    
    def __add__(self, other):
        return OrganicCell(self.cells + other.cells)
    
    def __sub__(self, other):
        try:
            if self.cells < other.cells:
                raise TypeError
            else:
                return OrganicCell(self.cells - other.cells)
        except TypeError:
            print('Ошибка уменьшения клетки! Вторая клетка не может быть больше первой')
    
    def __mul__(self, other):
        return OrganicCell(self.cells * other.cells)
    
    def __truediv__(self, other):
        return OrganicCell(self.cells // other.cells)

    def make_order(self, cells_per_row):
        return ('*' * cells_per_row + '\n') * (self.cells // cells_per_row) + '*' * (self.cells % cells_per_row)

cell1 = OrganicCell(15)
cell2 = OrganicCell(12)
cell3 = OrganicCell(20)
print(f'Данны две клетки: первая клетка содержит {cell1.cells} ячеек, вторая {cell2.cells} ячеек')
print(f'Сложения двух клеток: {cell1 + cell2}')
print(f'Уменьшение двух клеток: {cell1 - cell2}')
#тест не правильного уменьшения
print(cell1 - cell3)
print(f'Умножение двух клеток: {cell1 * cell2}')
print(f'Деление двух клеток: {cell1 / cell2}')
print(f'Структура клетки 1:\n{cell1.make_order(3)}')
print(f'Структура клетки 2:\n{cell2.make_order(5)}')
