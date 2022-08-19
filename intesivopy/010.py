valPed = float(input("Informe o valor pedido: "))
est = input("Para qual Estado é a entrega?: ").upper()
valImp = valPed * (5.5/100)
valTot = valPed + valImp
if est == 'PA':
    print("O subtotal do pedido é R${:.2f}.".format(valPed))
    print("O imposto é de R${:.2f}".format(valImp))
    print("O total do pedido é R${:.2f}".format(valTot))
else:
    print("O total do pedido é R${:.2f}".format(valTot))