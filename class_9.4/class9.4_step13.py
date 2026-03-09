# На вход программе подаётся строка текста.
# Напишите программу, которая выводит на экран символ, который появляется наиболее часто.

s = input()

counter = 0
result = ""

for i in s:
    if s.count(i) >= counter:
        counter = s.count(i)
        result = i

print(result)
