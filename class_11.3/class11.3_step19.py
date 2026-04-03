# На вход программе подаётся натуральное число n(n≥2). 
# Затем поступают n целых чисел. 
# Напишите программу, которая создаёт из указанных чисел список, состоящий из сумм соседних чисел.

n = int(input())

counter = 0

list = []

for i in range(n):
    n_digits = int(input())
    counter += n_digits
    list.append(counter)
    counter = n_digits
print(list[1:])

