# На вход программе подаются натуральное число n, а затем n целых чисел. 
# Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа. 
# Все числа должны быть выведены в том же порядке, в котором они были введены, каждое на отдельной строке.

n = int(input())

negative = []

positive = []

zero = []

for i in range(n):
    num = int(input())

    if num < 0:
        negative.append(num)
    elif num == 0:
        zero.append(num)
    else:
        positive.append(num)
print(*negative, sep='\n')
print(*zero, sep='\n')
print(*positive, sep='\n')