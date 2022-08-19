print("Digite C para Celsius.\nDigite F para Fahrenheit.")
temp = input("Digite sua escolha: ").upper()
if temp == 'C':
    tempC = input("Por favor, insira a temperatura em Celsius: ")
    if tempC.isnumeric():
        tempC = float(tempC)
        F = (tempC * 9 / 5) + 32
        print("A conversão da temperatura {}ºC em Fahrenheit é {:.1f}ºF.".format(tempC, F))
    else:
        print("Apenas números são permitidos.")
elif temp == 'F':
    tempF = input("Por favor, insira a temperatura em Fahrenheit: ")
    if tempF.isnumeric():
        tempF = float(tempF)
        C = (tempF - 32) * 5 / 9
        print("A conversão da temperatura {}ºF em Celsius é {:.1f}ºC.".format(tempF, C))
    else:
        print("Apenas números são permitidos.")
else:
    print("Opção Inválida.")