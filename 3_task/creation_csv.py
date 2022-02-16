def Go():
    creator_Adres_parents()
    creator_cab_csv()
    creator_Number()
    creator_stud_csv()

def creator_stud_csv():
    path = 'student.csv'
    with open(path, 'a') as data:
        data.write('id;Имя;Фамилия;Отчество;Год;Класс;Успеваемость;Дополнительно\n')
        data.write('')
        data.close()

def creator_cab_csv():
    path = 'cabinet.csv'
    with open(path, 'a') as data:
        data.write('Урок;Класс;id;Ряд;Парта;Вариант\n')
        data.write('')
        data.close()

def creator_Adres_parents():
    path = 'Adres_Parents.csv'
    with open(path, 'a') as data:
        data.write('id;Адрес проживания ученика;Адрес школы;Работа родителей\n')
        data.write('')
        data.close()

def creator_Number():
    path = 'Number.csv'
    with open(path, 'a') as data:
        data.write('id;Номер ученика;Номер родителей;Доп номер\n')
        data.write('')
        data.close()


