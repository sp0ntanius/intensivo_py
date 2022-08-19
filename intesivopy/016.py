list_imp = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
som = 0
for i in list_imp:
    if i > 5:
        som += i
print(list_imp)
print("A soma dos valores ímpares é {}.".format(som))