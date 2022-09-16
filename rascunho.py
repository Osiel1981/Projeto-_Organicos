produtos = {'maça':2.5, 'pera':3}

nome = input("digite o nome do produto")
valor = input("digite o valor do produto")
produtos[nome] = valor
 
print(produtos)
for nomes in produtos:
    print(nomes)
