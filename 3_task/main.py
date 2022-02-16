import controller as cnt
import creation_csv as crc
num = int(input('Введите 1 =>> что бы создать CSV \n'
'Введите 2 =>> что бы добавить нового ученика:\n '
'Введите 3 ==>> что бы добавить информацию о уроке\n'
': '))
if num == 1:
    crc.Go()
elif num == 2:
    cnt.write_file()
elif num == 3:
    cnt.class_file()