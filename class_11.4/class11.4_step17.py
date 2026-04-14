# На вход программе подаются натуральное число n, затем n строк, затем ещё одна строка – поисковый запрос. 
# Напишите программу, которая выводит все введённые строки, в которых встречается поисковый запрос.

n = int(input())
array = []

for i in range(n):
    array.append(input())

query = input().lower()

for s in array:
    if query in s.lower():
        print(s)
