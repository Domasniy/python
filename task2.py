def user(name, surname, birthday, city, email, phone):
    return f'Имя: {name}, Фамилия: {surname}, Год рождения: {birthday}, Город: {city}, Email: {email}, Телефон: {phone}'


print(user(name='Иван', surname='Иванов', birthday='1980', city='Москва', email='i.ivanov@email.ru', phone='+7999999999'))