# На вход программе подаётся одно число n. Напишите программу, которая выводит список [1, 2, 3, ..., n].

n = int(input())

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(abc[:n])

# another code

n = int(input())

s = ""
for i in range(n):
    s += chr(ord("a") + i)
    
print(list(s))