# Дано нечётное натуральное число n.
# Напишите программу, которая печатает равнобедренный звёздный треугольник с основанием, равным n, в соответствии с примером:
# *
# **
# ***
# ****
# ***
# **
# *

n = int(input())

for i in range(1, n // 2 + 2):
    print("*" * i)
for j in range(n // 2, 0, -1):
    print("*" * j)

# другое решение

n = int(input())

for i in range(n):
    cur_cnt = (n // 2 + 1) - abs(n // 2 - i)
    for j in range(cur_cnt):
        print("*", end="")
    print()
