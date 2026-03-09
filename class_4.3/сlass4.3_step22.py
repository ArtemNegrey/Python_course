# На числовой прямой даны два отрезка: [ a1;b1] и [a2;b2]. Напишите программу, которая находит их пересечение.
# Пересечением двух отрезков может быть:
# отрезок, точка, пустое множество

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a1 > a2:
    left = a1
else:
    left = a2
if b1 < b2:
    right = b1
else:
    right = b2

if left < right:
    print(left, right)
elif left == right:
    print(right)
else:
    print("пустое множество")
