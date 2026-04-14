# Дополните приведённый ниже код так, чтобы он вывел сумму квадратов элементов списка numbers.

numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]

sum = 0

for i in range (len(numbers)):
    summq = numbers[i] ** 2
    sum += summq
print(sum) 

# another code

numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]

square_numbers_sum = 0
for el in numbers:
    square_numbers_sum += el ** 2

print(square_numbers_sum)