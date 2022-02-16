import user_interfaife as UI
print('Если вы хотите добавить ученика введите его class и id, \n'
'если запустили программу первый раз пропустите эти два поля!')

print('id = уникальный номер ученика.')
id = UI.id()
full_id = id

def Go():
    stud_csv()
    Adres_parents()
    Number()

def stud_csv():
    global full_id
    path = 'student.csv'
    name = UI.name()
    surname = UI.surname()
    patr = UI.patronymic()
    year = UI.year_of_birth()
    clas = UI.clas()
    AcadPerf = UI.academic_performance()
    Dop = UI.bonus()
    with open(path, 'a') as data:
        data.write(f'{full_id};{name};{surname};{patr};{year};{clas};{AcadPerf};{Dop}\n')
        data.write('')
        data.close()

def cab_csv():
    global full_id
    Work = UI.work()
    clas = UI.clas()
    row = UI.row()
    desk = UI.desk()
    option = UI.option()
    path = 'cabinet.csv'
    with open(path, 'a') as data:
        data.write(f'{Work};{clas};{full_id};{row};{desk};{option}\n')
        data.write('')
        data.close()

def Adres_parents():
    global full_id
    path = 'Adres_Parents.csv'
    STadr = UI.student_address()
    SCadr = UI.school_address()
    PWo = UI.Parents_work()
    with open(path, 'a') as data:
        data.write(f'{full_id};{STadr};{SCadr};{PWo}\n')
        data.write('')
        data.close()

def Number():
    global full_id
    PNu = UI.parent_number()
    PNu2 = UI.parent_number2()
    STuN = UI.student_number()
    path = 'Number.csv'
    with open(path, 'a') as data:
        data.write(f'{full_id};{STuN};{PNu};{PNu2}\n')
        data.write('')
        data.close()

