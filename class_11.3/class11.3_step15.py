# На вход программе подаются натуральное число n, а затем n строк. 
# Напишите программу, которая создаёт из указанных строк список, а затем выводит его.

number = int(input())

list = []
for i in range(number):
    str = input()
    list.append(str)
    
print(list)