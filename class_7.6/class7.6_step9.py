# Дано натуральное число.
# Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

a = int(input())

last = a % 10

all_equal = True

while a > 0:
    digit = a % 10
    if digit != last:
        all_equal = False
        break
    a //= 10

if all_equal:
    print("YES")
else:
    print("NO")
