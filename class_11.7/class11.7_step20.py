# На вход программе подаётся строка текста. 
# Напишите программу, использующую списочное выражение, которая выводит все цифровые символы данной строки.

s = str(input())

symbols = [num for num in s if num in '1234567890']

print(*symbols, sep='')

# another code

digits = [s for s in input() if s.isdigit()]
print(*digits, sep="")