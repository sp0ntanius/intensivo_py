from random import randint
list_aleat = []
for c in range(0, 30):
    num = randint(0, 100)
    list_aleat.append(num)

print(list_aleat)

for i, elem in enumerate(list_aleat):
    if i == 20:
        print('O {}º termo é {}.'.format(i , elem))