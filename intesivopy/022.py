def calc(x, y, z):
    if z == '+':
        return x + y
    elif z == '-':
        return x - y
    elif z == 'x':
        return x * y
    elif z == '/':
        return x / y
while True:
    num1 = float(input("Informe um número: "))
    num2 = float(input("Informe um número: "))
    opc = input("Informe a operação que deseja ('+', '-', 'x', '/'): ")
    if opc != '+' and opc != '-' and opc != 'x' and opc != '/':
        while True:
            print("Opção inválida.")
            opc = input("Informe a operação que deseja ('+', '-', 'x', '/'): ")
            if opc == '+' or opc == '-' or opc == 'x' or opc == '/':
                break
    print("O resultado entre {} e {} com a operação desejada é {}.".format(num1, num2, calc(num1, num2, opc)))
    cont = input("Deseja continuar? (S/N): ").upper()
    if cont == 'S':
        continue
    elif cont == 'N':
        print("Obrigado por usar a calculadora!")
        break
    else:
        while cont != 'S' and cont != 'N':
            print("Opção inválida.")
            cont = input("Deseja continuar? (S/N): ").upper()