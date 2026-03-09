# На плоскости евклидово расстояние ρ между двумя точками (x1;y1) и (x2​; y2) и определяется так:
# p = корень из ((x1 - x2)^2 + (y1 - y2)^2)

import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

p1 = math.pow(x1 - x2, 2)
p2 = math.pow(y1 - y2, 2)

p3 = p1 + p2

p = math.sqrt(p3)

print(p)

# Другое решение

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
distance = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

print(distance)
