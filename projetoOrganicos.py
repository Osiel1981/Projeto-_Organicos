
from re import A
carrinho = 0

somaCarrinho = 0

produtos = dict()

Estoque = [{'maça':2.5, 'pera':3}]

preco = 0


print('''
                  =====================================
                  !!! Bem Vindo ao Desefio Organicos!!!
                  =====================================
                  =====================================
                  =                                   =
                  =             .-------.             =
                  =            _|_O_    |_            =
                  =           |         | |           =
                  =           | .-------' |           =
                  =           |_|    _____|           =
                  =             |     O |             =
                  =             '-------'             =
                  =                                   =
                  =====================================
                  =        Primeiro Projeto           =
                  =               do                  =
                  =     Div Magalu : Dev - Python     =
                  =====================================
                  =  Desnvolvedores:                  =
                  =                                   =
                  =                Anderson Teixeira  =
                  =                Eron Morais        =
                  =                João Paulo Garcia  =
                  =                Osiel Mesquita     =
                  ===================================== 
                  =                                   =
                  = Orientação :                      =
                  =                                   =
                  =                  Matheus Willian  =
                  =                                   =
                  =====================================
                  =                                   =
                  ===================================== 



 
''')

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

    opcao = input("Digite o que deseja acessar: ")
    
    if opcao.upper() == 'C':

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
    
        
        if opcao.upper() == 'C':
            
            novo_produto = input("Qual o nome do novo produto: ")
            while len(novo_produto) <= 2:
                print("nome não pode conter menos de 2 caracteres'.")
                input("Favor inserir um nome válido")
            produtos['produto'] = novo_produto
            
            preco_produto = float(input("Qual o preço atualizado? \nR$:"))
            while preco_produto <= 0:
                print("Valor deve ser maior que R$ 0")
                input("Favor inserir valor válido: R$")
            produtos['preco'] = preco_produto
            Estoque.append(produtos.copy())
        else:
            print("opção ainda não cadastrada")

        print(Estoque)


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
                    produto = input(
                        "Digite o nome do produto que deseja adicionar ao carrinho: ")
                    if produto in produtos.keys():

                        carrinho = carrinho + produtos[produto]

                    else:
                        print('''
                        ------------------------
                        Esse produto não existe!
                        ------------------------
                        ''')

                    maisCarrinho = input(
                        "Deseja adicionar mais produtos ao carrinho? Digite S para sim ou N para não: ")

            if opcaoVendas.upper() == "R":
                menosCarrinho = "S"
                while menosCarrinho == "S":
                    produto = input(
                        "Digite o nome do produto que deseja remover: ")

                    carrinho = carrinho - produtos(produto)

                    menosCarrinho = input(
                        "Deseja remover mais produtos do carrinho? Digite S para sim ou N para não ")


print('''
_______________
Fim de programa!
_______________
''')
print(carrinho)
