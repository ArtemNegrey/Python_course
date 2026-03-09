# Дано натуральное число.
# Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.

a = int(input())

flag = False

counter = 0

while a != 0:
    last_digit = a % 10
    if last_digit >= counter:
        flag = True
        counter = last_digit
    else:
        flag = False
        break
    a = a // 10
if flag == True:
    print("YES")
else:
    print("NO")
