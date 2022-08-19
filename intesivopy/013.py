from random import randint
qlqr = randint(1,100)
print("Tente adivinhar um número entre 1 a 100.")
chute = int(input("Qual é o seu palpite? "))
i = 0
while True:
    if chute < qlqr:
        print("Errou, tente um número maior que {}.".format(chute))
        chute = int(input("Qual é o seu palpite? "))
        i += 1
    elif chute > qlqr:
        print("Errou, tente um número menor que {}.".format(chute))
        chute = int(input("Qual é o seu palpite? "))
        i += 1
    else:
        i += 1
        print("Parabéns! Você acertou o número em {} tentativas.".format(i))
        break