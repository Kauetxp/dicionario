dicionario = {"Gato":"Chat","cachorro":"Chien","Cavalo":"Cheval"}
palavras = ['Gato','Lion','Cavalo']

for palavra in palavras:
    if palavra in dicionario:
        print(palavra,"==>",dicionario[palavra])
    else:
        print(palavra,"Não está no dicionário")
        
