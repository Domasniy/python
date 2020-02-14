class Date():

    def __init__(self, date):
        Date.date = date    

    @classmethod
    def date_print(cls):
        date_list = list(map(int,cls.date.split('-')))
        if Date.date_validate(date_list):
            print(f'День: {date_list[0]}\nМесяц: {date_list[1]}\nГод: {date_list[2]}')
            return date_list


    @staticmethod
    def date_validate(date):
        if date[0] > 31 or date[0] < 1:
            print(f'Число дня не может быть меньше 1 и больше 31. У объекта заданно: {date[0]}')
            return False
        if date[1] > 12 or date[1] < 1:
            print(f'Число месяца не может быть меньше 1 и больше 31. У объекта заданно: {date[1]}')
            return False
        return True

date1 = Date('10-06-2017')
date1.date_print()

#Не правильный день
date2 = Date('44-06-2017')
date1.date_print()
#Не правильный месяц
date2 = Date('13-14-2017')
date1.date_print()


