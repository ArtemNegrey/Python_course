# Напишите программу, определяющую площадь круга и длину окружности по заданному радиусу R.
import math

r = float(input())

s = math.pi * pow(r, 2)
c = 2 * math.pi * r
print(s)
print(c)
