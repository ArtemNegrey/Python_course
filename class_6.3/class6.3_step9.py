# В математике выделяют следующие средние значения:
# среднее арифметическое чисел a, b = (a+b)/2
# среднее геометрическое чисел a, b = sqrt(a*b)
# среднее гармоническое чисел a, b = (2ab)/(a+b)
# среднее квадратичное чисел a, b = sqrt(a^2+b^2)/2

from math import *

a = float(input())
b = float(input())

average_arif = (a + b) / 2
average_geom = sqrt(a * b)
average_garm = (2 * a * b) / (a + b)
average_sqrt = sqrt((pow(a, 2) + pow(b, 2)) / 2)

print(average_arif)
print(average_geom)
print(average_garm)
print(average_sqrt)
