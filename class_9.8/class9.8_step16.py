# Все книги в домашней библиотеке Душнилы, друга Сэма, должны быть обязательно отсортированы по возрастанию:
# сначала по фамилиям авторов, а в случае совпадения фамилий – по названиям.
# Напишите программу, которая проверяет, верно ли отсортированы книги.
# На вход программе подаются число n, а затем – n строк, каждая строка представляет собой книгу в следующем формате:
# <фамилия автора> <инициалы автора>, «<название книги>»
# Программа должна вывести «YES» (без кавычек), если книги отсортированы в соответствии с пожеланиями Душнилы, или «NO» (без кавычек) в противном случае.

n = int(input())
answer = "YES"

s1 = input()
space_pos = s1.find(" ")
surname1 = s1[:space_pos]
start = s1.find("«")
end = s1.find("»")
title1 = s1[start + 1 : end]

for i in range(n - 1):
    s2 = input()
    space_pos2 = s2.find(" ")
    surname2 = s2[:space_pos2]
    start2 = s2.find("«")
    end2 = s2.find("»")
    title2 = s2[start2 + 1 : end2]

    if surname2 < surname1 or (surname2 == surname1 and title2 < title1):
        answer = "NO"
        break

    surname1 = surname2
    title1 = title2

print(answer)

# Другое решение

n = int(input())

# переменные для хранения предыдущей фамилии автора и названия книги
previous_book = ""
# переменная флага указывает, сохранен ли порядок сортировки книг:
is_ordered = "YES"

for i in range(n):
    s = input()
    # извлекаем фамилию автора до первого пробела
    current_surname = s[: s.find(" ")]
    # извлекаем название книги между кавычками «»
    current_title = s[s.find("«") + 1 : s.rfind("»")]
    # склеиваем фамилию автора и название книги
    current_book = current_surname + current_title

    # если текущая книга меньше предыдущей
    # то порядок сортировки нарушен
    if current_book < previous_book:
        is_ordered = "NO"

    # обновляем предыдущие значения книги на текущие
    previous_book = current_book

print(is_ordered)
