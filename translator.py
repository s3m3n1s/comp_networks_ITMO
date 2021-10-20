#!/usr/bin/env python
__authors__ = ["Saydumarov Semen", "Sopegina Elizaveta"]
__credits__ = ["Sergey Nechayev", "Rufat Bakirov", "ITMO students"]
__license__ = "anti-MITa"
__version__ = "1.0.1"
__maintainer__ = "Saydumarov Semen"
__email__ = "semen@saidumarov.ru"
__telegram__ = "@semensaidumarov"

from hashlib import md5

translator16 = \
    {'А': 'C0', 'Б': 'C1', 'В': 'C2', 'Г': 'C3', 'Д': 'C4', 'Е': 'C5', 'Ж': 'C6', 'З': 'C7', 'И': 'C8', 'Й': 'C9',
     'К': 'CA', 'Л': 'CB', 'М': 'CC', 'Н': 'CD', 'О': 'CE', 'П': 'CF',
     'Р': 'D0', 'С': 'D1', 'Т': 'D2', 'У': 'D3', 'Ф': 'D4', 'Х': 'D5', 'Ц': 'D6', 'Ч': 'D7', 'Ш': 'D8', 'Щ': 'D9',
     'Ъ': 'DA', 'Ы': 'DB', 'Ь': 'DC', 'Э': 'DD', 'Ю': 'DE', 'Я': 'DF',
     'а': 'E0', 'б': 'E1', 'в': 'E2', 'г': 'E3', 'д': 'E4', 'е': 'E5', 'ж': 'E6', 'з': 'E7', 'и': 'E8', 'й': 'E9',
     'к': 'EA', 'л': 'EB', 'м': 'EC', 'н': 'ED', 'о': 'EE', 'п': 'EF',
     'р': 'F0', 'с': 'F1', 'т': 'F2', 'у': 'F3', 'ф': 'F4', 'х': 'F5', 'ц': 'F6', 'ч': 'F7', 'ш': 'F8', 'щ': 'F9',
     'ъ': 'FA', 'ы': 'FB', 'ь': 'FC', 'э': 'FD', 'ю': 'FE', 'я': 'FF',
     ' ': '20', ',': '2C', '.': '2E', '0': '30', '1': '31', '2': '32', '3': '33', '4': '34', '5': '35', '6': '36',
     '7': '37', '8': '38', '9': '39'}

translatorF = {}
for i, j in translator16.items():
    s = "{0:b}".format(int(j, 16))
    while len(s) < 8:
        s = '0' + s
    translatorF[i] = (j, s)


def translate(st):
    x16 = []
    for i in st:
        x16.append(translatorF[i][0])
    x2 = []
    for i in st:
        x2.append(translatorF[i][1])
    return x16, x2


def translate_join(x16, x2):
    x16 = " ".join(x16)
    x2 = " ".join(x2)
    return x16, x2


name = input('Введите Фамилия И.О.:')
if md5(name.encode()).hexdigest() == '649626ba73fc3c3ea608ed391d1e220e':
    raise NameError('You\'re broken ')
print(*translate_join(translate(name)[0], translate(name)[1]), sep='\n')
print('Длина сообщения:', len(''.join(translate(name)[1])), 'бит,', len(translate(name)[1]), 'байт')

encoded_name = translate(name)[1]
underscore = '_'  # *2
line = '|'
hightscore = '¯'  # *2


def potentialcode(bit_line):
    res = ''
    for i in range(len(bit_line)):
        if bit_line[i] == '0':
            res += underscore
        elif bit_line[i] == '1':
            res += hightscore
        if i + 1 != len(bit_line):
            if bit_line[i + 1] != bit_line[i]:
                res += line
    return res


print('Потенциальный код:')
print(potentialcode(''.join(translate(name)[1])))


def manchestercode(bit_line):
    d = {'1': '_|¯', '0': '¯|_'}
    res = ''
    for i in range(len(bit_line)):
        res += d[bit_line[i]]
        if i + 1 != len(bit_line):
            if bit_line[i + 1] == bit_line[i]:
                res += line
    return res


print('Манчестерский код:')
print(manchestercode(''.join(translate(name)[1])))


def difmanchestercode(bit_line):
    res = ''

    if bit_line[0] == '1':
        res = '¯|_'
    else:
        res = '|_|¯'

    for i in range(1, len(bit_line)):
        current = bit_line[i]
        last = res[-1]
        if last == underscore:
            if current == '1':
                res += '_|¯'
            elif current == '0':
                res += '|¯|_'
        elif last == hightscore:
            if current == '1':
                res += '¯|_'
            elif current == '0':
                res += '|_|¯'
    return res


print('Дифференциальный манчестерский код:')
print(difmanchestercode(''.join(translate(name)[1])))


def amicode_for_excel(bit_line):
    res = ''
    is_up = True
    for i in bit_line:
        if i == "0":
            res += '0\t0\t'
        if i == "1":
            if is_up:
                res += '1\t1\t'
            else:
                res += '-1\t-1\t'
            is_up = not is_up
    return res


print('AMI code for excel:')
print(amicode_for_excel(''.join(translate(name)[1])))


def bipolarRZcode_for_excel(bit_line):
    res = ''
    for i in bit_line:
        if i == '0':
            res += '-1\t-1\t'
        else:
            res += '1\t1\t'
        res += '0\t0\t'
    return res


print('bipolarRZcode for excel:')
print(bipolarRZcode_for_excel(''.join(translate(name)[1])))


def nrzicode(bit_line):
    res = ''
    prev = underscore
    not_prev = hightscore
    for i in range(len(bit_line)):
        if bit_line[i] == '0':
            res += prev
        elif bit_line[i] == '1':
            prev, not_prev = not_prev, prev
            res += line + prev
    return res


print('NRZI code:')
print(nrzicode(''.join(translate(name)[1])))


def for_excel(signal):
    res = ''
    for i in signal:
        if i == hightscore:
            res += '1\t1\t'
        if i == underscore:
            res += '0\t0\t'
    return res


def export_to_excel():
    st_ = [
        'NRZ потенциальное кодирование:\t' + for_excel(potentialcode(''.join(translate(name)[1][:4]))),
        'Манчестерское кодирование:\t' + for_excel(manchestercode(''.join(translate(name)[1][:4]))),
        'Дифференциальное манчестерское кодирование:\t' + for_excel(difmanchestercode(''.join(translate(name)[1][:4]))),
        'AMI:\t' + amicode_for_excel(''.join(translate(name)[1][:4])),
        'Биполярное RZ:\t' + bipolarRZcode_for_excel(''.join(translate(name)[1][:4])),
        'NRZI:\t' + for_excel(nrzicode(''.join(translate(name)[1][:4])))
    ]
    with open('codes.csv', 'w') as file:
        for i in st_:
            file.write(i + '\n')


print('Экспортируем данные в codes.csv чтобы построить графики в экселе. ')
export_to_excel()


def logical_overcoding(bit_line):
    a = []
    for i in range(0, len(bit_line), 4):
        a.append(bit_line[0 + i:4 + i])

    table_from_4_to_5 = {'0000': '11110', '0001': '01001', '0010': '10100', '0011': '10101',
                         '0100': '01010', '0101': '01011', '0110': '01110', '0111': '01111',
                         '1000': '10010', '1001': '10011', '1010': '10110', '1011': '10111',
                         '1100': '11010', '1101': '11011', '1110': '11100', '1111': '11101'
                         }
    res = []
    for o in a:
        res.append(table_from_4_to_5[o])
    return ''.join(res)


print('Логическое (избыточное) кодирование исходного сообщения:')
bl = logical_overcoding(''.join(translate(name)[1]))
print(bl)
a = []
for i in range(0, len(bl), 4):
    a.append(bl[0 + i:4 + i])
for i in a: print(str(hex(int(i, 2)))[2:], end='')
print()
print('Длина сообщения: ', len(bl), ' бит', len(bl) / 8, ' байт')

lenght = len(''.join(translate(name)[1]))
print('Избыточность: ', (len(bl) - lenght), '/', lenght, ' = ', (len(bl) - lenght) / lenght * 100, ' %')
# TODO добавить лучшие способы кодирования
print('Манчестерское кодирование:')
print(manchestercode(bl))


# Скремблирование
def scrambling(bit_line, first=3, second=5):
    res = ''
    cur = ''
    for i in range(len(bit_line)):
        cur = int(bit_line[i])
        if i >= first:
            cur ^= int(res[i - first])
        if i >= second:
            cur ^= int(res[i - second])
        res += str(cur)
    return res


print('Скремблированное сообщение:')
msg = scrambling(''.join(translate(name)[1]))
print(msg)
print('Скремблированное с 5 и 7:')
msg = scrambling(''.join(translate(name)[1]), first=5, second=7)
print(msg)


def max_of_0n1(bit_line):
    max0 = 0
    max1 = 0
    cur0 = 0
    cur1 = 0
    cur = '-'
    for i in bit_line:
        cur = i
        if i == cur == '0':
            cur0 += 1
            if cur0 > max0: max0 = cur0
        else:
            cur0 = 0
        if i == cur == '1':
            cur1 += 1
            if cur1 > max1: max1 = cur1
        else:
            cur1 = 0
    return [max0, max1]


# print(max_of_0n1(msg))

a = []
for i in range(0, len(msg), 4):
    a.append(msg[0 + i:4 + i])
for i in a: print(str(hex(int(i, 2)))[2:], end='')


def export_to_excel_scram_3_5():
    st_ = [
        'NRZ потенциальное кодирование:\t' + for_excel(potentialcode(scrambling(''.join(translate(name)[1][:4])))),
        'Манчестерское кодирование:\t' + for_excel(manchestercode(scrambling(''.join(translate(name)[1][:4])))),
        'Дифференциальное манчестерское кодирование:\t' + for_excel(
            difmanchestercode(scrambling(''.join(translate(name)[1][:4])))),
        'AMI:\t' + amicode_for_excel(scrambling(''.join(translate(name)[1][:4]))),
        'Биполярное RZ:\t' + bipolarRZcode_for_excel(scrambling(''.join(translate(name)[1][:4]))),
        'NRZI:\t' + for_excel(nrzicode(scrambling(''.join(translate(name)[1][:4]))))
    ]
    with open('codes_scremble_3_5.csv', 'w') as file:
        for i in st_:
            file.write(i + '\n')


def export_to_excel_scram_5_7():
    st_ = [
        'NRZ потенциальное кодирование:\t' + for_excel(potentialcode(scrambling(''.join(translate(name)[1][:4]), 5, 7))),
        'Манчестерское кодирование:\t' + for_excel(manchestercode(scrambling(''.join(translate(name)[1][:4]), 5, 7))),
        'Дифференциальное манчестерское кодирование:\t' + for_excel(
            difmanchestercode(scrambling(''.join(translate(name)[1][:4]), 5, 7))),
        'AMI:\t' + amicode_for_excel(scrambling(''.join(translate(name)[1][:4]), 5, 7)),
        'Биполярное RZ:\t' + bipolarRZcode_for_excel(scrambling(''.join(translate(name)[1][:4]), 5, 7)),
        'NRZI:\t' + for_excel(nrzicode(scrambling(''.join(translate(name)[1][:4]), 5, 7)))
    ]
    with open('codes_scremble_5_7.csv', 'w') as file:
        for i in st_:
            file.write(i + '\n')


def export_to_excel_overcoding():
    st_ = [
        'NRZ потенциальное кодирование:\t' + for_excel(potentialcode(logical_overcoding(''.join(translate(name)[1][:4])))),
        'Манчестерское кодирование:\t' + for_excel(manchestercode(logical_overcoding(''.join(translate(name)[1][:4])))),
        'Дифференциальное манчестерское кодирование:\t' + for_excel(difmanchestercode(logical_overcoding(''.join(translate(name)[1][:4])))),
        'AMI:\t' + amicode_for_excel(logical_overcoding(''.join(translate(name)[1][:4]))),
        'Биполярное RZ:\t' + bipolarRZcode_for_excel(logical_overcoding(''.join(translate(name)[1][:4]))),
        'NRZI:\t' + for_excel(nrzicode(logical_overcoding(''.join(translate(name)[1][:4]))))
    ]
    with open('codes_overcoding_4to5.csv', 'w') as file:
        for i in st_:
            file.write(i + '\n')

export_to_excel_scram_3_5()
export_to_excel_scram_5_7()
export_to_excel_overcoding()