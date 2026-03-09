# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел

total = 1
for i in range(10):
    num = int(input())
    if num != 0:
        total *= num
print(total)
