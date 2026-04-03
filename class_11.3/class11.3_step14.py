# Напишите программу, выводящую следующий список: ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]

list = []

for i in range(26):
    list.append(chr(ord('a') + i)*(i+1))
print(list)