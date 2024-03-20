import csv

'''подключение бибиотеки для чтения и записи в .csv'''

def rd():

    '''
    Описание функции rd().
        Функция открывает файл и разбивает содержащуюся в нем информацию на списки для дальнейшей работы с ней.

    Описание переменных.
        sp - двумерный список - вся содержащаяся в файле информация
        crs - двумерный список - избавляет от ненужной информации, содержит только данные в формате [компания, должность, зарплата]
    '''

    with open('vacancy.csv', encoding="utf8") as f:
        f.readline()
        sp = [i[:-2].split(';') for i in f.readlines()]
        crs = [[sp[i][4], sp[i][3], int(sp[i][0])] for i in range(len(sp))]
        crs = sorted(crs, reverse = True, key = lambda x: x[2])
    wr(crs)

def wr(crs):

    '''
    Описание функции wr()
        Функция записи в новый фвйл
    
    Описание аргументов
        crs - двумерный список - данные которые необходимо обработать и записать
    '''

    with open('vacancy_new.csv', 'w', newline = '', encoding='utf8') as csvnew:
        w = csv.DictWriter(csvnew, fieldnames = ['company', 'role', 'Salary'], delimiter = ';')
        w.writeheader()
        buff = []
        rows = []
        for i in crs:
            if not(crs[0] in buff):
                row = {'company' : i[0], 'role' : i[1], 'Salary' : i[2]}
                rows.append(row)
            else:
                buff.append(crs[0])
        w.writerows(rows)

    for i in range(3):
        print(rows[i]['company'], rows[i]['role'], rows[i]['Salary'], sep = ' - ')

rd()