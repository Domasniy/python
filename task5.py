class Stationery:

    def __init__(self, title):
        self.title = title
    
    def draw(self):
        print('Запуск отрисовки')
    
class Pen(Stationery):
    
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        print('Пишем ручкой')

class Pencil(Stationery):
    
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        print('Пишем карандашом')   

class Handle(Stationery):
    
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        print('Пишем маркером')


station1 = Pen('Ручка')
station1.draw()
station2 = Pencil('Карандаш')
station2.draw()
station3 = Handle('Маркер')
station3.draw()