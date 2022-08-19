usuarioR = 'lula2022'
senhaR = 'uniaoflasco2022'
usu = None
sen = None
i = 1
while i <= 4:
    usu = input("Informe o nome de Usuário: ")
    sen = input("Informe a senha: ")
    if usu == usuarioR and sen == senhaR:
        print("Acesso Concedido.")
        break
    else:
        print("Usuário ou senha incorretos.")
    if i == 3:
        print("Número de tentivas esgotadas.")
        break        
    i += 1