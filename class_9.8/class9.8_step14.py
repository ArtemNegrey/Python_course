# На вход программе подаются 3 различных слова.
# Вам необходимо отсортировать эти слова по возрастанию в лексикографическом порядке и вывести их на одной строке, разделяя символом пробела.

a = input()
b = input()
c = input()

max_word = max(a, b, c)
min_word = min(a, b, c)

if a != min_word and a != max_word:
    mid_word = a
elif b != min_word and b != max_word:
    mid_word = b
else:
    mid_word = c
print(min_word, mid_word, max_word, sep=" ")
