# Напишите функцию print_symbol_counts(s), 
# которая принимает на вход слово s и выводит для каждой буквы этого слова в лексикографическом порядке 
# в нижнем регистре на отдельной строке количество её вхождений в это слово в следующем формате:
# <L>: <N>
# где <L> – некоторая буква слова s, <N> – количество вхождений этой буквы в слово s.

def print_symbol_counts(s):
    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for letter in sorted(count):
        print(f"{letter}: {count[letter]}")

s = input().lower()

print_symbol_counts(s)