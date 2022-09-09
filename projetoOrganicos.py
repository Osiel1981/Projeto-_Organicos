from re import A
produtos = dict()
Estoque = []
preco = 0



print('''
==================================
Bem Vindo ao Desefio Organicos!!!
==================================''')

opcao = "a"
while opcao.upper() != "S": 
    print('''
    -----------------
    Menu de navegação
    C = cadastro
    V = vendas 
    R = Relatórios
    S = sair e feixar o programa
    -----------------''')

    opcao = input("Digite o que deseja acessar: ").upper()

    if opcao == 'C':
        novo_produto = input("Qual o nome do novo produto")
        while len(novo_produto) <= 5:
            print("nome não pode conter menos de 5 caracteres'.")
            input("Favor inserir um nome válido")
        produtos['produto'] = novo_produto

        preco_produto = float(input("Qual o preço atualizado? \nR$:"))
        while preco_produto <= 0:
            print("Valor deve ser maior que R$ 0")
            input("Favor inserir valor válido: R$")
        produtos['preco'] = preco_produto


        Fabricante = input("Qual o fabricante do produto: \n")
        while len(Fabricante) <= 2:
            print("Valor inválido")
            input("Favor inserir nome válido:\n")
        produtos['fabricante'] = Fabricante

        fornecedor = input("Qual o nome do fornece:\n")
        while len(fornecedor) <= 3:
            print("Valor inválido")
            input("Favor inserir nome válido:\n")
        produtos['fornecedor'] = fornecedor
        Estoque.append(produtos.copy())
        print("Produto cadastrado, :", novo_produto)
        print(Estoque)
    else:
        print("opção ainda não cadastrada")

print("Fim de program")
