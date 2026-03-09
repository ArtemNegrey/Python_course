# Напишите программу, которая упорядочивает три числа от большего к меньшему.

a = int(input())
b = int(input())
c = int(input())

max_digit = max(a, b, c)
min_digit = min(a, b, c)
mid_digit = a + b + c - max_digit - min_digit

print(max_digit)
print(mid_digit)
print(min_digit)
