import psycopg2

print('1. Добавить клиента \n2. Добавить номер телефона для клиента \n3. Изменение данных клиента \n4. Удалить номер телефона у клиента \n5. Удалить клиента \n6. Найти клиента по данным')
clien_search = input('Введите номер для команды: ')












conn = psycopg2.connect(dbname='postgres', user='postgres', password='1111', host='127.0.0.1', port='5432')
cursor = conn.cursor()

if clien_search == '1':
    name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    email = input('Введите почту: ')
    telephone = input('Введите телефон (Если не хотите вписывать, номер напишите 0: ')
    if telephone == '0':
        telephone = None
    people = (name, last_name, email, telephone)
    cursor.execute("INSERT INTO telephone_book (name, last_name, email, telephone) VALUES(%s, %s, %s, %s)", people)

elif clien_search == 2:
    telephones = input('Введите номер телефона который хотите добавить')
    id_cl = input('Введите id клиета для которого добавляется телефон')
    telep = (telephones, id_cl)
    cursor.execute("UPDATE telephone_book SET telephone = %s WHERE id=%s", telep)

# cursor.execute('CREATE TABLE telephone_book (id SERIAL PRIMARY KEY, name VARCHAR(50), last_name VARCHAR(50), email VARCHAR(100), telephone VARCHAR(12))')
# conn.commit() #подтверждение транкзации
# print('ТАБЛИЦА СОЗДАНА')

# people = ('Иван', 'Никитин', 'IvanN2@mail.ru', None)
# cursor.execute("INSERT INTO telephone_book (name, last_name, email, telephone) VALUES(%s, %s, %s, %s)", people)

# telep = ('89378759075', 2)
# cursor.execute("UPDATE telephone_book SET telephone = %s WHERE id=%s", telep)

# telep = (None, 2)
# cursor.execute("UPDATE telephone_book SET telephone = %s WHERE id=%s", telep)

# id_delete = (1,)
# cursor.execute("DELETE FROM telephone_book WHERE id=%s", id_delete)

# client_id = [('Никитин')]
# cursor.execute("SELECT * FROM telephone_book WHERE last_name=%s", client_id)
# print(cursor.fetchall())


conn.commit()


cursor.close()
conn.close()
