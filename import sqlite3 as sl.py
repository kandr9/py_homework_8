import sqlite3 as sl
from easygui import *

conn = sl.connect('telbook.db')

cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS contacts
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            tNumber TEXT,
            mail TEXT,
            birthday TEXT)
            ''')


def add_values():
    name=enterbox("Введите имя контакта:")
    tNumber=enterbox("Введите телефонный номер:")
    mail=enterbox("Введите электронную почту:")
    birthday=enterbox("Введите дату рождения:")
    cur.execute("INSERT INTO contacts (name, tNumber, mail, birthday ) VALUES (?, ?, ?, ?)", (name, tNumber, mail, birthday))
    conn.commit()
    msgbox("Контакт добавлен.")


def select_all():
    cur.execute('SELECT * FROM contacts')
    output=''
    for row in cur.fetchall():
        output+=str(row)
    msgbox(output, 'Существующие контакты')


def search_contact():
    keyword=enterbox("Введите искомое значение:")
    cur.execute ('SELECT * FROM contacts WHERE name LIKE ? OR tNumber LIKE ? OR mail LIKE ? OR birthday LIKE ?' , ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
    output=''
    for row in cur.fetchall():
        output+=str(row)
    msgbox(output, 'Найденные контакты')


def edit_contact():
    nameToEdit=enterbox("Введите контакт для редактирования:")
    while True:
        edit_choice = choicebox("Выберите поле для редактирования", "Главная форма", ['Имя', 'Номер телефона', 'Электронная почта', 'Дата рождения',  'Выход'])
        if edit_choice == "Имя":
            newname=enterbox("Введите новое имя контакта:")
            cur.execute("UPDATE  contacts SET name=? WHERE name=?", (newname, nameToEdit))
        conn.commit()

        if edit_choice == "Номер телефона":
            newtNumber=enterbox("Введите новый номер телефона:")
            cur.execute("UPDATE  contacts SET tNumber=? where name=?", (newtNumber, nameToEdit))
        conn.commit()

        if edit_choice == "Электронная почта":
            newMail=enterbox("Введите новый адрес электронной почты:")
            cur.execute("UPDATE  contacts SET mail=? where name=?", (newMail, nameToEdit))
        conn.commit()

        if edit_choice == "Дата рождения":
            newBirthday=enterbox("Введите новую дату рождения:")
            cur.execute("UPDATE  contacts SET birthday=? where name=?", (newBirthday, nameToEdit))
        conn.commit()    

        if edit_choice == "Выход":
            break

    conn.commit()
    msgbox("Контакты  отредактирован.")


def main():
        while True:
            choice = choicebox("Выберите действие", "Главная форма", ['Просмотр контактов',  'Добавить контакт', 'Изменить контакт', 'Поиск', 'Выход'])

            if choice == "Просмотр контактов":
                select_all()

            if choice == "Добавить контакт":
                add_values()

            if choice == "Изменить контакт":
                edit_contact()

            if choice == "Поиск":
                search_contact()  

            if choice == "Выход":
                break

        conn.close()

if __name__=='__main__':
     main()
