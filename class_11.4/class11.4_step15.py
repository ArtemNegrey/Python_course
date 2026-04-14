# На вход программе подаются натуральное число n, а затем n целых чисел. 
# Напишите программу, которая для каждого введённого числа x выводит значение функции f(x)=x^2+2x+1, каждое на отдельной строке.

n = int(input())

func_array = []

for i in range (n):
    new_n = int(input())
    new_func_n = new_n ** 2 + 2 * new_n + 1
    func_array.append(new_func_n)
    print(new_n)
print()
print(*func_array, sep='\n')

