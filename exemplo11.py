agenda = {}

while True:
    nome = input("Digite o nome da pessoa: ")
    if nome == "":
        break
    telefone = input("Digite o telefone: ")
    
    #Adicionando ao dicionario
    
    agenda[nome] = telefone
    
#Pesquisa um telefone na agenda

nomepesquisa = input("Digite um nome para pesquisar: ")
if nomepesquisa in agenda:
    print("Telefone de",nomepesquisa,":",agenda[nomepesquisa])
else:
    print("Nome não encontrado")
    

