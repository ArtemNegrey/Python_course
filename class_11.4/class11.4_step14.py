# На вход программе подаются натуральное число n, а затем n строк. 
# Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.

n = int(input())
array = []

for i in range (n):
    s = str(input())
    if s not in array:
        array.append(s)
print(*array, sep='\n')
