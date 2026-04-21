# На вход программе подаётся строка текста, содержащая различные натуральные числа. 
# Вам необходимо переставить максимальный и минимальный элементы местами и вывести изменённую строку.

s = input()

new_s = s.split()

numbers = [int(x) for x in new_s]

min_value = min(numbers)
max_value = max(numbers)

min_index = numbers.index(min_value)
max_index = numbers.index(max_value)

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print(*numbers)