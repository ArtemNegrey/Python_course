# Дано натуральное число n(n≥10).
# Напишите программу, которая определяет его максимальную и минимальную цифры и выводит текст в следующем формате:
# Максимальная цифра равна <максимальная цифра>
# Минимальная цифра равна <минимальная цифра>

a = int(input())
counter = 0
max_value = 0
min_value = 9

while a > 0:
    counter = a % 10
    if counter > max_value:
        max_value = counter
    if counter < min_value:
        min_value = counter
    a = a // 10
print("Максимальная цифра равна", max_value)
print("Минимальная цифра равна", min_value)

# Другое решение

n = int(input())
max_digit = 0
min_digit = 9

while n > 0:
    cur_digit = n % 10

    max_digit = max(max_digit, cur_digit)
    min_digit = min(min_digit, cur_digit)

    n //= 10

print("Максимальная цифра равна", max_digit)
print("Минимальная цифра равна", min_digit)
