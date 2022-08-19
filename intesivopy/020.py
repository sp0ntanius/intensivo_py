list_not = []
for c in range(0,4):
    notas = float(input("Informe a sua {}ª nota: ".format(c + 1)))
    if notas > 0 and notas < 11:
            list_not.append(notas)
    else:
        while notas < 0 or notas> 10:
            print("Nota não permitida.")
            notas = float(input("Insira novamente a {}ª nota: ".format(c + 1)))
            if notas > 0 and notas < 11:
                list_not.append(notas)
print("A média das notas informadas é {:.2f}.".format(sum(list_not) / len(list_not)))