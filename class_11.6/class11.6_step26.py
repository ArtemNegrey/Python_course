# На вход программе подаётся строка текста, содержащая целые числа. 
# Из данной строки формируется список чисел. 
# Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию.

s = input()

numbers = s.split()
int_lst = [int(x) for x in numbers]

int_lst.sort()
print(*int_lst)

int_lst.sort(reverse=True)
print(*int_lst)