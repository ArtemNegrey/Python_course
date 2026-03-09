# На вход программе подаётся натуральное число n.
# Напишите программу, которая выводит для каждой четной цифры данного числа текст в следующем формате:
# <i>-я четная цифра равна <digit>где <i> – номер четной цифры (начиная с 1), <digit> – значение четной цифры.
# При этом если в числе нет четных цифр, необходимо вывести следующий текст:Четных цифр в числе нет

n = input()
counter = 0
i = 0

while i < len(n):
    digit = int(n[i])
    if digit % 2 == 0:
        counter += 1
        print(f"{counter}-я четная цифра равна {digit}")
    i += 1

if counter == 0:
    print("Четных цифр в числе нет")

# another code

n = int(input())
digits = len(str(n))
even_cnt = 0
for i in range(1, digits + 1):
    digit = n // 10 ** (digits - i) % 10
    if digit % 2 == 0:
        even_cnt += 1
        print(str(even_cnt) + "-я", "четная цифра равна", digit)

if even_cnt == 0:
    print("Четных цифр в числе нет")
