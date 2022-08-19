opc = 0
num1 = 0
num2 = 0
for i in range(0, 9999999999):
    num1 = input("Digite um número: ")
    if num1.isnumeric():
        num1 = float(num1)
        num2 = input("Digite outro número: ")
        if num2.isnumeric():
            num2 = float(num2)
            opc = input("Digite uma opção (+, -, *, /):")
            if opc == '+':
                print("A adição entre {} e {} é {}.".format(num1, num2, num1 + num2))
            elif opc == '-':
                print("A subtração entre {} e {} é {}.".format(num1, num2, num1 - num2))
            elif opc == '*':
                print("A multiplicação entre {} e {} é {}.".format(num1, num2, num1 * num2))
            elif opc == '/':
                print("A divisão entre {} e {} é {}.".format(num1, num2, num1 / num2))
            else:
                print("Opção inválida.")
        else:
            while num2.isalpha():
                print("Opção inválida.")
                num2 = input("Digite outro número: ")
    else:
        while num1.isalpha():
            print("Opção inválida.")
            num1 = input("Digite um número: ")