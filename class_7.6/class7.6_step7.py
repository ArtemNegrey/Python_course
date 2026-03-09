# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

a = int(input())
original = a

sum_digits = 0
count_digits = 0
mult_digits = 1

last_digit_of_number = a % 10

while a != 0:
    last_digit = a % 10
    sum_digits += last_digit
    count_digits += 1
    mult_digits *= last_digit
    first_digit = last_digit
    a = a // 10
average_of_digits = sum_digits / count_digits
sum_first_last = first_digit + last_digit_of_number
print(sum_digits)
print(count_digits)
print(mult_digits)
print(average_of_digits)
print(first_digit)
print(sum_first_last)
