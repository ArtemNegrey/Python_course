# Напишите программу, которая определяет наименьшее из четырёх чисел.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

smallest = a

if b < smallest:
    smallest = b
if c < smallest:
    smallest = c
if d < smallest:
    smallest = d
print(smallest)
