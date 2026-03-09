# На вход программе подаётся натуральное число n.
# Напишите программу, которая вычисляет значение выражения (1 + 1/2 ​+ 1/3 ​+…+ 1/n​)−ln(n)
from math import log

n = int(input())
total = 0
num = 0

for i in range(n):
    num = 1 / (n - i)
    total += num
print(total - log(n))
