class Warehouse():
    
    def __init__(self, location, storage_space):
        self.inventory = {Printer: [], Scanner: [], Monitor: []}
        self.location = location
        self.storage_space = storage_space
    
    def store(self, *items, amount=1):
        found = False
        try:
            if type(amount) != int:
                raise ValueError
        
            for i in items:
                for item in self.inventory[i.__class__]:
                    if item[0] == i:
                        item[1] += amount
                        found = True
                        break
                if not found:    
                    self.inventory[i.__class__].append([i,amount])
                print(f'На склад принят {i.type_name} - {i.model}. В количестве {amount} ед.')
        except ValueError:
            print('Не удалось принять на склад. Количество должно быть указано в числовом формате')
    
    def sent(self, department, *items, amount):
        for i in items:
            for item in self.inventory[i.__class__]:
                if item[0] == i:
                    item[1] -= amount
                    print(f'Со склада передали {i.type_name} - {i.model}. В количестве {amount} ед.\n На складе осталось: {item[1]} ед.') 
                    break
    

class Hardware():
    
    def __init__(self, model, vendor, weight):
        self.model = model
        self.vendor = vendor
        self.weight = weight

class Printer(Hardware):
    type_name = 'принтер'
    def __init__(self, model, vendor, weight, is_color, print_speed):
        super().__init__(model, vendor, weight)
        self.is_color = is_color
        self.print_speed = print_speed
    


class Scanner(Hardware):
    type_name = 'сканнер'
    def __init__(self, model, vendor, weight, scan_speed, have_adf):
        super().__init__(model, vendor, weight)
        self.scan_speed = scan_speed
        self.have_adf = have_adf


class Monitor(Hardware):
    type_name = 'монитор'
    def __init__(self, model, vendor, weight, matrix_size, matrix_resolution):
        super().__init__(model, vendor, weight)
        self.matrix_size = matrix_size
        self.matrix_resolution = matrix_resolution

warehouse1 = Warehouse('Москва',100)
printer1 = Printer('HP 426dn', 'HP', 10, False, 20)
scanner1 = Scanner('Epson 1200', 'Epson', 5, 15, True)
monitor1 = Monitor('Benq X2411', 'Benq', 9, 24, '1920x1800')

warehouse1.store(printer1, scanner1, monitor1, amount = 10)
warehouse1.sent('Отдел продаж',printer1, monitor1, amount = 5)

warehouse1.store(printer1, scanner1, monitor1, amount = 'fdfd')

