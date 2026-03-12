# Под "тяжестью" слова будем понимать сумму кодов по таблице Unicode всех символов этого слова.
# Напишите программу, которая принимает 4 слова и находит среди них самое тяжёлое слово.
# Если самых тяжёлых слов будет несколько, то программа должна вывести первое из них.

word1 = input()
word2 = input()
word3 = input()
word4 = input()

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0

for i in word1:
    counter1 += ord(i)
for i in word2:
    counter2 += ord(i)
for i in word3:
    counter3 += ord(i)
for i in word4:
    counter4 += ord(i)
if counter1 >= counter2 and counter1 >= counter3 and counter1 >= counter4:
    print(word1)
elif counter2 >= counter3 and counter2 >= counter4:
    print(word2)
elif counter3 >= counter4:
    print(word3)
else:
    print(word4)
