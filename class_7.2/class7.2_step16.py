# Даны два целых числа m и n (m>n). Напишите программу, которая выводит все нечётные целые числа от m до n (включительно) в порядке убывания.

# без if
m = int(input())
n = int(input())

for i in range(m - (m + 1) % 2, n - 1, -2):
    print(i)

# c if

m = int(input())
n = int(input())

if m % 2 != 0:
    for i in range(m, n - 1, -2):
        print(i)
else:
    for i in range(m - 1, n - 1, -2):
        print(i)
