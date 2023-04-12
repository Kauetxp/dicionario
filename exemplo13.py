products = {
    "Banana":2.50,
    "Maça":3.00,
    "Laranja": 2.75,
    "Abacaxi": 4.50,
    "Manga": 3.50
}

#Imprimir o preço de uma maça
print("O preço de uma maçã é: R$" + str(products["Maça"]))

#Adiciona um novo produto
products["Melancia"] = 6.00

#Imprimir todos os itens
for product,price in products.items():
    print(product+": R$"+str(price))
    
    