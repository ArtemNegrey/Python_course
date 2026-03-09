# На вход программе подаётся строка текста.
# Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.

s = input()

endcom = s.endswith(".com")
endru = s.endswith(".ru")

if endcom or endru == True:
    print("YES")
else:
    print("NO")

# Другое решение

s = input()

if s.endswith(".com") or s.endswith(".ru"):
    print("YES")
else:
    print("NO")
