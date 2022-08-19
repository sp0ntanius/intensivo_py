import requests
real = float(input("Insira a quantidade de reais que deseja converter: R$"))

r = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

req_dol_json = r.json()
    
cot_dol = float(req_dol_json["USDBRL"]["bid"])
cot_eur = float(req_dol_json["EURBRL"]["bid"])

print("A conversão de R${} para dólar é USD${:.2f}.".format(real, real / cot_dol,))
print("A conversão de R${} para euro é EUR${:.2f}.".format(real, real / cot_eur))







'''res = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")
print(res)

res_json = res.json()
print(res_json)

cot_dol = float(res_json["USDBRL"]["bid"])
print(cot_dol)'''