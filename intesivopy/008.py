idd = int(input("Digite a sua idade: "))
if idd < 18:
    print("Você precisa ser maior de idade para participar dos cursos.")
else: 
    cnh = int(input("1 - Sim / 2 - Não\nVocê tem CNH?: "))
    if cnh == 1:
        print("Você pode participar dos cursos de:\nDireção Defensiva e Defesa Pessoal.")
    elif cnh == 2:
        print("Você pode participar apenas do curso de Defesa Pessoal.")
    else:
        print("Opção inválida.")