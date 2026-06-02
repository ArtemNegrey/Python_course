# Напишите функцию print_sorted_hyphen(s), которая принимает строку s, состоящую из слов, 
# разделённых дефисами, и выводит эти слова на одной строке в лексикографическом порядке, разделённые дефисами.

def print_sorted_hyphen(s):
    s = s.split('-')
    s.sort()

    print(*s, sep='-')

s = input()

print_sorted_hyphen(s)