# Дано натуральное число n. Напишите программу, которая выводит значение суммы:
# 1!+2!+3!+…+n!

from math import *

n = int(input())
summ = 0

for x in range(1, n + 1):
    summ += factorial(x)
print(summ)
