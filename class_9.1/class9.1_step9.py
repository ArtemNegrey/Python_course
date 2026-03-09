# На вход программе подаются три строки: имя, фамилия и отчество (именно в таком порядке).
# Напишите программу, которая выводит инициалы человека.

name = str(input())
surname = str(input())
fathername = str(input())

print(surname[0], name[0], fathername[0], sep="")
