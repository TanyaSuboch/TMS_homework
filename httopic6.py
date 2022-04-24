import json
import csv
import pandas as pd
import openpyxl
from csv import writer

#дз по презентации 6

#задание 1
def make_string():
    b = b'r\xc3\xa9sum\xc3\xa9'
    s = b.decode("utf-8")
    print(s)
    t = s.encode("Latin1")
    print(t)
    k = t.decode("Latin1")
    print(k)

#задание 2
def create_file():
    a = 'London is the capital of Great Britain'
    b = 'Berlin is the capital of Germany'
    c = 'Minsk is the capital of Belarus'
    d = 'Paris is the capital of France'
    f = open('country_capital.txt', 'w')
    f.write(a)
    f.write('\n')
    f.write(b)
    f.close
    f = open('country_capital.txt', 'a')
    f.write('\n')
    f.write(c)
    f.write('\n')
    f.write(d)
    f.close

#задание 3
def create_dictionary():
    #dictionary = {id(int): (name(str), age(int))}
    dictionary = {123456: ("Lena", 23),
    589364: ("Katya", 29),
    742358: ("Andrey", 34),
    364971: ("Ira", 19),
    201367: ("Nikita", 27),
    953810: ("Sergey", 21)
    }
    with open("name_age.json", "w") as write_file:    
        json.dump(dictionary, write_file)

#задание 4

def convert_from_json_to_csv():
    df = pd.read_json(r'C:\Users\TanyaS\Downloads\TMS_homework\name_age.json')
    df.to_csv(r'C:\Users\TanyaS\Downloads\TMS_homework\name_age_phone.csv', index = None)
    with open("name_age_phone.csv", "a", newline="") as a_object:
        new_row_data = ['265-19-89', '352-98-41', '625-14-03', '452-30-87', '304-65-91', '438-20-95']
        writer_object = writer(a_object)
        writer_object.writerow(new_row_data)
        a_object.close()


def add_column():
    x = open(r'C:\Users\TanyaS\Downloads\TMS_homework\name_age_phone.csv')
    y = csv.reader(x)
    z = []
    for row in y:
        z.append(['0']+row)
    #w=csv.writer(x)
    #data[0][0]=" "
    #for row in data:
    #    w.writerow(row)
    del z[0][0]
    del z[1][0]
    del z[2][0]
    del z[3][0]
    z[0].insert(0 ,'id')
    z[1].insert(0, 'name')
    z[2].insert(0, 'age')
    z[3].insert(0, 'phone')
    x.close
    print(z)

#тут отображается с новой колонкой в терминале, но не сохраняет в файл
#[['id', '123456', '589364', '742358', '364971', '201367', '953810'], 
# ['name', 'Lena', 'Katya', 'Andrey', 'Ira', 'Nikita', 'Sergey'], 
# ['age', '23', '29', '34', '19', '27', '21'], 
# ['phone', '265-19-89', '352-98-41', '625-14-03', '452-30-87', '304-65-91', '438-20-95']]


#задание 5*

#только сохранение из csv в excel
def convert_csv_into_excel(): 
    read_file = pd.read_csv (r'C:\Users\TanyaS\Downloads\TMS_homework\name_age_phone.csv')
    read_file.to_excel (r'C:\Users\TanyaS\Downloads\TMS_homework\name_age_phone.xlsx', 
    index = None, header=True)


if __name__ == '__main__':
    convert_csv_into_excel()