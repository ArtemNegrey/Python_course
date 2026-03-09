# Напишите программу, вычисляющую значение тригонометрического выражения sinX + cosX + tg^2 X по заданному числу градусов x

from math import *

x = float(input())

r = radians(x)

result = sin(r) + cos(r) + pow(tan(r), 2)

print(result)
