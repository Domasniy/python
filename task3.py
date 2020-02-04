class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, "bonus": bonus}
    
class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    
    def get_full_name(self):
        return self.name + ' ' + self.surname
    
    def get_total_income(self):
        return int(self._income['wage']) + int(self._income['bonus'])

worker1 = Position('Вася', 'Пупкин', 'Дворник', 20000, 5000)

print(f'Имя: {worker1.name}\nФамилия: {worker1.surname}\nДолжность: {worker1.position}\nЗарплата: {worker1._income["wage"]} руб.\nПремия: {worker1._income["bonus"]} руб.')
print(f'Полное Имя: {worker1.get_full_name()}')
print(f'Всего заработал: {worker1.get_total_income()} рублей')
    
