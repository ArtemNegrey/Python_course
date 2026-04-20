# На вход программе подаётся строка текста, содержащая фамилию, имя и отчество человека. 
# Напишите программу, которая выводит инициалы человека.

full_name = input()

new_full_name = full_name.split()

for i in range(len(new_full_name)):
    print(new_full_name[i][0], end='.')