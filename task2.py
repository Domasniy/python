class Road:

    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)
    
    def calculate_mass(self):
        return print(f'Для покрытия дороги длинной {self._length} метров и шириной {self._width} метров нужно : {int(self._length * self._width * 25 * 5/1000)} тонн асфальта')

a = Road(5000,20)
a.calculate_mass()