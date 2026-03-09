# У Тимура есть список никнеймов соцсети FriendsGram. Напишите программу, которая выводит первый никнейм, не содержащий символ нижнего подчёркивания _.

while True:
    nickname = input()
    if "_" not in nickname:
        print(nickname)
        break
