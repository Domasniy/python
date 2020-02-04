from random import choice

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        print(f'Машина "{self.name}" поехала')

    def stop(self):
        print(f'Машина "{self.name}" остановилась')

    def turn(self,direction):
        print(f'Машина "{self.name}" повернула {direction}')
    
    def show_speed(self):
        print(f'Текущая скорость "{self.name}": {self.speed}')

class TownCar(Car):
    
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    
    def show_speed(self):
        print(f'Текущая скорость "{self.name}": {self.speed}')
        if self.speed > 60:
            print(f'Вы привышаете скорость')

class SportCar(Car):
    
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    

class WorkCar(Car):
    
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    
    def show_speed(self):
        print(f'Текущая скорость "{self.name}": {self.speed}')
        if self.speed > 40:
            print(f'Вы привышаете скорость')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    

car1 = WorkCar(60, 'Красная', 'Погрузчик', False)
car1.go()
car1.turn(choice(['вправо','влево','на шоссе', 'во двор']))
car1.show_speed()
car1.speed = 35
car1.show_speed()

car2 = SportCar(120, 'Зеленая', 'Молния', False)
car2.go()
car2.turn(choice(['вправо','влево','на шоссе', 'во двор']))
car2.show_speed()