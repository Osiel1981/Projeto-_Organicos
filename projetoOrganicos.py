
carrinho = 0

somaCarrinho = 0

from re import A
produtos = dict()
Estoque = ['maça':2.5, 'pera':3]
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

    S = sair e fechar o programa
    -----------------''')
    opcao = input("Digite o que deseja acessar: ").upper()
    
    if opcao == 'C':
        print('''
    -----------------
    Menu de Cadastro
    C = Cadastramento de produtos
    L = Listar produtos cadastrados 
    D = Deleção de produtos
    V = Voltar para o menu anterior
    S = Sair do programa
    -----------------''')
    
    opcao = input("Digite o que deseja acessar: ")
    if not opcao.upper() in "CVRS": 
        
        print('''
        _______________
        OPÇÃO INVALIDA
        _______________''')
    
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



       


    if opcao.upper() == "V":
        opcaoVendas = "V"
        while opcaoVendas.upper() in "VAR":

            print('''
            ---------------------------
             Bem Vindo ao Menu de Vendas
            ---------------------------
             ''')
            opcaoVendas = input('''
            Digite A se deseja adicionar um item ao seu carrinho de compras:
            Digite R se deseja remover um item do seu carrinho de compras:
            Digite S para voltar para o menu inicil
            ''')

            if opcaoVendas.upper() == "A":
                maisCarrinho = "S"

                while maisCarrinho.upper() == "S":
                    produto = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
                    if produto in produtos.keys():
                    
                        carrinho = carrinho + produtos[produto]

                    else:
                        print('''
                        ------------------------
                        Esse produto não existe!
                        ------------------------
                        ''')


                    maisCarrinho = input("Deseja adicionar mais produtos ao carrinho? Digite S para sim ou N para não: ")

            if opcaoVendas.upper() == "R":
                menosCarrinho = "S"
                while menosCarrinho == "S":
                    produto = input("Digite o nome do produto que deseja remover: ")
                    
                    carrinho = carrinho - produtos(produto)

                    menosCarrinho = input("Deseja remover mais produtos do carrinho? Digite S para sim ou N para não ")




print('''
_______________
Fim de programa!
_______________
''')
print(carrinho)

