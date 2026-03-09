# На вход программе подаётся натуральное число n.
# Напишите программу вычисления знакочередующейся суммы: 1−2+3−4+5−6+…+(−1)^n+1 * n

n = int(input())
counter = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        counter -= i
    else:
        counter += i
print(counter)
