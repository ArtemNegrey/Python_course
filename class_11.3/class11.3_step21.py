# На вход программе подаются натуральное число n и n строк, а затем число k. 
# Напишите программу, которая выводит k-ую букву из введённых строк на одной строке без пробелов.

n = int(input())
cloud = []

for i in range(n):
    cloud.append(input())

k = int(input())

result = ''

for s in cloud:
    if len(s) >= k:
        result += s[k - 1]

print(result)