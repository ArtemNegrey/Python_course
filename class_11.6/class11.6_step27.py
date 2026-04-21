# На вход программе подаются число n, 
# а затем – n песен из плейлиста Сэма, каждая на отдельной строке. 
# Напишите программу, которая сортирует эти песни в алфавитном порядке и выводит каждую из них на отдельной строке.

n = int(input())
songs_array = []

for i in range(n):
    songs = input()
    songs_array.append(songs)
songs_array.sort()
print(*songs_array, sep='\n')
