# n школьников делят k мандаринов поровну, неделящийся остаток остается в корзине. Сколько целых мандаринов достанется каждому школьнику? Сколько целых мандаринов останется в корзине?

schoolboy = int(input())
mandarins = int(input())
schoolboyMandarins = mandarins // schoolboy
mandarinsStay = mandarins % schoolboy
print(schoolboyMandarins)
print(mandarinsStay)
