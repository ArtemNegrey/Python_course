# На вход программе подаются натуральное число n, затем n строк, затем число k – количество поисковых запросов, затем k строк – поисковые запросы. 
# Напишите программу, которая выводит все введённые строки, в которых встречаются одновременно все поисковые запросы.

n = int(input())
array = []

for i in range(n):
    text = input()
    array.append(text)

k = int(input())
queries = []

for i in range(k):
    query = input()
    queries.append(query.lower())

for s in array:
    s_lower = s.lower()
    found_all = True

    for q in queries:
        if q not in s_lower:
            found_all = False
            break

    if found_all:
        print(s)