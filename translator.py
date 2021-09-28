# alf = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'.upper()+'абвгдежзийклмнопрстуфхцчшщъыьэюя ,.0123456789'
# x16 = 'CDEF2'
# x16p2 = '0123456789ABCDEF'
# d = {}
# for i in range(len(x16)):
#     for j in range(len(x16p2)):
#         try:
#             d[alf[i*16+j]]=x16[i]+x16p2[j]
#         except:
#             pass
# print(d)
translator16 = \
{'А': 'C0', 'Б': 'C1', 'В': 'C2', 'Г': 'C3', 'Д': 'C4', 'Е': 'C5', 'Ж': 'C6', 'З': 'C7', 'И': 'C8', 'Й': 'C9', 'К': 'CA', 'Л': 'CB', 'М': 'CC', 'Н': 'CD', 'О': 'CE', 'П': 'CF',
 'Р': 'D0', 'С': 'D1', 'Т': 'D2', 'У': 'D3', 'Ф': 'D4', 'Х': 'D5', 'Ц': 'D6', 'Ч': 'D7', 'Ш': 'D8', 'Щ': 'D9', 'Ъ': 'DA', 'Ы': 'DB', 'Ь': 'DC', 'Э': 'DD', 'Ю': 'DE', 'Я': 'DF',
 'а': 'E0', 'б': 'E1', 'в': 'E2', 'г': 'E3', 'д': 'E4', 'е': 'E5', 'ж': 'E6', 'з': 'E7', 'и': 'E8', 'й': 'E9', 'к': 'EA', 'л': 'EB', 'м': 'EC', 'н': 'ED', 'о': 'EE', 'п': 'EF',
 'р': 'F0', 'с': 'F1', 'т': 'F2', 'у': 'F3', 'ф': 'F4', 'х': 'F5', 'ц': 'F6', 'ч': 'F7', 'ш': 'F8', 'щ': 'F9', 'ъ': 'FA', 'ы': 'FB', 'ь': 'FC', 'э': 'FD', 'ю': 'FE', 'я': 'FF',
 ' ': '20', ',': '2C', '.': '2E', '0': '30', '1': '31', '2': '32', '3': '33', '4': '34', '5': '35', '6': '36', '7': '37', '8': '38', '9': '39'}

translatorF = {}
for i, j in translator16.items():
    s = "{0:b}".format(int(j, 16))
    while len(s)<8:
        s = '0'+s
    translatorF[i] = (j, s)


def translate(st):
    x16 = []
    for i in st:
        x16.append(translatorF[i][0])
    x2 = []
    for i in st:
        x2.append(translatorF[i][1])
    return (x16,x2)

name = 'Сайдумаров С.К.'#input()
print(translate(name))

underscore = '_'#*2
line = '|'
hightscore = '¯'#*2


def potentialcode(bit_line):
    for i in range(len(bit_line)):
        if bit_line[i] == '0': print(underscore, end='')
        elif bit_line[i] == '1': print(hightscore, end='')
        if i+1!=len(bit_line):
            if bit_line[i+1] != bit_line[i]: print(line, end ='')
    print()

print('Потенциальный код:')
potentialcode(''.join(translate(name)[1]))


def manchestercode(bit_line):
    d = {'1' :'_|¯', '0':'¯|_'}
    for i in range(len(bit_line)):
        print(d[bit_line[i]], end ='')
        if i+1!=len(bit_line):
            if bit_line[i+1] == bit_line[i]: print(line, end ='')
    print()

print('Манчестерский код:')
manchestercode(''.join(translate(name)[1]))

#TODO Еще способов кодирования накидать