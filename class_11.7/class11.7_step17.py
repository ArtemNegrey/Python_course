# На вход программе подаётся строка текста, содержащая слова. 
# Напишите программу, которая выводит слова введённой строки в столбик.

print(*input().split(), sep='\n')

# another code

words = [word for word in input().split()]
print(*words, sep='\n')