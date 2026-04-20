# На вход программе подаётся строка текста, содержащая 4 целых неотрицательных числа, разделённых точкой. 
# Напишите программу, которая определяет, является ли введённая строка текста корректным ip-адресом.

ip_address = input()
new_ip_address = ip_address.split('.')
counter = 0
for i in range(len(new_ip_address)):
    if 0 <= int(new_ip_address[i]) <= 255:
        counter += 1
    else:
        break
if counter == 4:
    print("ДА")
else:
    print("НЕТ")

# another code

seq = input().split(".")

for el in seq:
    if not (0 <= int(el) <= 255):
        print("НЕТ")
        break
else:
    print("ДА")