# На вход программе подаются 2 строки. 
# Вам необходимо сравнить эти строки посимвольно, не учитывая регистр и игнорируя все небуквенные символы. 
# Программа должна вывести «YES» (без кавычек), если строки окажутся равны в результате такой проверки, или «NO» (без кавычек) в противном случае.

word1 = input()
word2 = input()

new_word1 = ''
new_word2 = ''

for i in range(len(word1)):
    if word1[i].isalpha():
        new_word1 += word1[i]
for j in range(len(word2)):
    if word2[j].isalpha():
        new_word2 += word2[j]
if new_word1.lower() == new_word2.lower():
    print('YES')
else:
    print('NO')