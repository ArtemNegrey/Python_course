# На вход программе подаётся строка текста. 
# Напишите программу, которая определяет, является ли введённая строка корректным телефонным номером. 
# Строка текста является корректным телефонным номером, если она соответствует одному из следующих форматов:
# abc-def-hijk
# 7-abc-def-hijk
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.
# Программа должна вывести «YES» (без кавычек), если строка является корректным телефонным номером, или «NO» (без кавычек) в противном случае.

s = input()

parts = s.split('-')

if len(parts) == 3:
    if len(parts[0]) == 3 and len(parts[1]) == 3 and len(parts[2]) == 4:
        if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

elif len(parts) == 4:
    if parts[0] == '7':
        if len(parts[1]) == 3 and len(parts[2]) == 3 and len(parts[3]) == 4:
            if parts[1].isdigit() and parts[2].isdigit() and parts[3].isdigit():
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')

else:
    print('NO')
