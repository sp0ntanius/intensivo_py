from datetime import date
print("Informe quando começam as aulas.")
data1 = int(input("Informe o dia: "))
data2 = int(input("Informe o mês: "))
data3 = int(input("Informe o ano: "))
data_comc = date(data3, data2, data1)
data_at = date.today()
delta_comc_at = data_comc - data_at
if delta_comc_at.days > 0:
    print("Faltam {} dias para começarem as aulas.".format(delta_comc_at.days))
elif delta_comc_at.days == 0:
    print("As aulas começam hoje!")
else:
    print("As aulas já começaram, vagabundo!")