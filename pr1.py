from encodings import utf_8


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


while True:
    try:
        file = open('pr1FIO.txt','a', encoding = 'utf8')

        try:              
            surname, name, middlename, year = (i for i in input().split(' '))
            if surname == '0' and name == '0' and middlename == '0' and year == '0':
                break
            elif isint(year) and len(year) == 4: 
                file.write(str(surname) + ' ' + str(name) + ' ' + str(middlename) + ' ' + str(year) + ' ' + '\n')

            else:
                print('Дата должна состоять из 4-х цифр')

        except ValueError:
            print('введите данные правильно!')

        finally:
            file.close()
    except:
        print('Ошибка открытия файла')


print('Фамилия Имя Отчество Год рождения')
num: int = 1
try:
    file = open('pr1FIO.txt', 'r', encoding = 'utf8')
    while True:
        line = file.readline()
        if not line:
            break
        print('Фамилия ' + str(num) + ' Имя ' + str(num) + ' Отчество ' + str(num) + ' Год рождения ' + str(num) + '\n')
        print(str(line))
        num += 1
except:
    print('Ошибка открытия файла')
finally:
    file.close()
 