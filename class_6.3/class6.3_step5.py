# Напишите программу, которая принимает на вход действительное число x и вычисляет по нему значение: ⌊x⌋+⌈x⌉
import math

a = float(input())

f = math.floor(a)
c = math.ceil(a)

print(f + c)
