from datetime import *
idd_at = int(input("Digite a sua idade atual: "))
idd_apo = int(input("Digite a idade que você gostaria de se aposentar: "))
delta = idd_apo - idd_at
print("Ainda faltam {} anos para você se aposentar.".format(delta))
print("É {}, então você se aposentará em {}.".format(datetime.now().year,  datetime.now().year+ idd_apo))