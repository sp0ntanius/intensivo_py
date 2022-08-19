from random import randint, uniform
list_alt = []
list_idd = []
maior_13 = 0
abaixo_med = 0
for i in range(0,30):
    num1 = randint(10, 70)
    list_idd.append(num1)
    num2 = uniform(1.0, 2.0)
    list_alt.append(num2)
for c in list_idd:
    if c > 13:
        maior_13 += 1
for d in list_alt:
    if d < (sum(list_alt) / len(list_alt)):
        abaixo_med += 1
print(list_idd)
print(list_alt)
print("Houve {} pessoas com idade acima de 13 anos,\ne houve {} pessoas abaixo da média de altura.".format(maior_13, abaixo_med))