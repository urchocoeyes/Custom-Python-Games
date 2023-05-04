import psycopg2
import csv

connect = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="nn22913705"
)


def function_for_checking_of_user(name, surname, tel):
    flag = False
    if len(name) == 0:
        flag = True
    elif name[0] >= 'a' and name[0] <= 'z':
        flag = True
    elif len(surname) == 0:
        flag = True
    elif surname[0] >= 'a' and surname[0] <= 'z':
        flag = True
    elif len(tel) != 12:
        flag = True
    elif tel[0:2] != "+7":
        flag = True
    if flag:
        return True
    else:
        return False


def function_for_adding_user(name, surname, tel):
    cur.execute(f"SELECT * FROM some_data WHERE name = '{name}' and surname = '{surname}'")
    data = cur.fetchall()
    if len(data) == 0:
        cur.execute(f"INSERT INTO some_data (name,surname, tel) VALUES ('{name}', '{surname}' , '{tel}')")
        print("Successfully entered into database.")
    else:
        cur.execute(
            f"UPDATE some_data SET name = '{name}', surname = '{surname}', tel = '{tel}' WHERE name = '{name}' and surname = '{surname}'")
        print("Successfully updated data of database.")
    connect.commit()


list_of_function = ["1 - ENTER A NEW USER", "2 - CHANGE DATA OF USER", "4 - DELETE USER",
                    "5 - INSERT DATA By CSV FILE", "6 - SORTING BY NAME", "7 - SORTING BY SURNAME",
                    "8 - SORTING BY TELEPHONE",
                    "W - SEARCH DATA BY PATTERN NAME", "Q - SEARCH DATA BY PATTERN SURNAME",
                    "E - SEARCH DATA BY PATTERN TELEPHONE",
                    "R - ENTERING INTO DATA SEVERAL USERS", "T - GET A DATA OF SEVERAL USERS",
                    "0 - TURN OF THE DATABASE"]

cur = connect.cursor()
go_to = "SOME"
while go_to != "STOP":
    for i in range(len(list_of_function)):
        if i % 2 == 0:
            print()
        print(list_of_function[i], end=" | ")
    print()
    go_to = input()

    if go_to == "1":
        for i in range(10):
            print()
        print("Enter a name: ")
        name = input()
        print("Enter a surname: ")
        surname = input()
        print("Enter a phone number: ")
        tel = input()
        if function_for_checking_of_user(name, surname, tel):
            print("Внесенные данные не верные")
        else:
            function_for_adding_user(name, surname, tel)
    elif go_to == "2":
        for i in range(10):
            print()
        print("Смена имени пользователя: ")
        print("Введите пожалуйста ваш номер телефона: ")
        tel_change = input()
        print("Спасибо")
        print("Введите имя на которую хотите сменить: ")
        name = input()
        print("Введите фамилию на которую хотите сменить: ")
        surname = input()
        cur.execute(f"UPDATE some_data SET name = '{name}', surname = '{surname}' WHERE tel = '{tel_change}'")
        print("Успешно изменен.")
        connect.commit()
    elif go_to == "4":
        for i in range(10):
            print()
        print("Удаление пользователя: ")
        print("По каким данным хотите удалить?")
        print("Введите 1 если по телефону")
        print("Введите любой знак кроме 1 если по имени и фамилии")
        key_buttom = input()
        if key_buttom == '1':
            print("Пожалуйста введите номер телефона который хотите удалить: ")
            tel = input()
            if not function_for_checking_of_user("Ramazan", "Syrlybay", tel):
                cur.execute(f"DELETE FROM some_data WHERE tel = '{tel}'")
                print("Success")
                connect.commit()
            else:
                print("Wrong data entered")

        else:
            for i in range(10):
                print()
            print("Enter a name: ")
            name = input()
            print("Enter a surname: ")
            surname = input()
            if not function_for_checking_of_user(name, surname, "+77028098386"):
                cur.execute(f"DELETE FROM some_data WHERE name = '{name}' AND surname = '{surname}'")
                print("Success")
                connect.commit()
            else:
                print("Wrong data entered")
    elif go_to == "5":
        for i in range(10):
            print()
        file = open("data.csv", "r")
        file = csv.reader(file)
        next(file)
        for value in file:
            cur.execute(f"INSERT INTO some_data (name, surname, tel) VALUES ('{value[0]}', '{value[1]}', '{value[2]}')")
        connect.commit()
    elif go_to == "6":
        for i in range(10):
            print()
        print("Sorting by name of the table: ")
        cur.execute("SELECT * FROM some_data ORDER BY name")
        data = cur.fetchall()
        for row in data:
            print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10}")
    elif go_to == "7":
        for i in range(10):
            print()
        print("Sorting by surname of the table: ")
        cur.execute("SELECT * FROM some_data ORDER BY surname")
        data = cur.fetchall()
        for row in data:
            print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10}")
    elif go_to == "8":
        for i in range(10):
            print()
        print("Sorting by telephone number of the table: ")
        cur.execute("SELECT * FROM some_data ORDER BY tel")
        data = cur.fetchall()
        for row in data:
            print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10}")
    elif go_to == "q":
        for i in range(10):
            print()
        print('Поиск по паттерну фамилии: ')
        print("Введите паттерн для фамилии: ")
        pattern_for_surname = input()
        cur.execute(f"SELECT * FROM some_data WHERE surname LIKE '{pattern_for_surname + '%'}'")
        data = cur.fetchall()
        for i in data:
            print(f"{i[0]:<10} {i[1]:<15} {i[2]:<10}")
    elif go_to == "w":
        for i in range(10):
            print()
        print('Поиск по паттерну имени: ')
        print("Введите паттерн для имени: ")
        pattern_for_name = input()
        cur.execute(f"SELECT * FROM some_data WHERE name LIKE '{pattern_for_name + '%'}'")
        data = cur.fetchall()
        for i in data:
            print(f"{i[0]:<10} {i[1]:<15} {i[2]:<10}")
    elif go_to == "e":
        for i in range(10):
            print()
        print('Поиск по паттерну номера телефона: ')
        print("Введите паттерн для номера телефона: ")
        pattern_for_tel = input()
        cur.execute(f"SELECT * FROM some_data WHERE tel LIKE '{pattern_for_tel + '%'}'")
        data = cur.fetchall()
        for i in data:
            print(f"{i[0]:<10} {i[1]:<15} {i[2]:<10}")
    elif go_to == 'r':
        for i in range(10):
            print()
        print("Внесение несколько людей в базу данных")
        print("Сколько людей вы бы хотели добавить в базу данных?")
        number = int(input())
        print("Принято")
        some_list_for_wrong_user = []
        for i in range(number):
            print(f"Внесите данные для {i + 1} пользователя: ")
            print("Enter a name: ")
            name = input()
            print("Enter a surname: ")
            surname = input()
            print("Enter a phone number: ")
            tel = input()
            if function_for_checking_of_user(name, surname, tel):
                some_list_for_wrong_user.append(name + "_" + surname)
            else:
                function_for_adding_user(name, surname, tel)
        if len(some_list_for_wrong_user) != 0:
            print("Пользователи, которые не были внесены в базу данных: ")
            for i in range(len(some_list_for_wrong_user)):
                print(some_list_for_wrong_user[i], end=" ")
                if i % 2 == 0:
                    print()
    elif go_to == "t":
        for i in range(10):
            print()
        print("Получить данные в отрывке database")
        print("Введите сколько пользователей хотите получить?: ")
        how_much = int(input())
        print("Спасибо")
        print("С какого места хотите эти данные получить?: ")
        start_pos = int(input())
        print("Thank you")
        print("Вот ваши данные: ")
        cur.execute(f"SELECT * from some_data")
        list_of_data = cur.fetchall()
        for i in range(start_pos, start_pos + how_much):
            print(f"{list_of_data[i][0]:<10} {list_of_data[i][1]:<15} {list_of_data[i][2]:<10}")

    elif go_to == "0":
        for i in range(10):
            print()
        print("Stopped")
        go_to = "STOP"
        cur.close()
        connect.close()
