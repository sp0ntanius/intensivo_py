from random import randint
list_aleat = []
for c in range(0,5):
    num = randint(0, 100)
    list_aleat.append(num)
for i, elem in enumerate(list_aleat):
    print("{}º vetor contém o número {}.".format(i + 1, elem))