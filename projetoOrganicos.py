
from re import A
carrinho = 0
produto = dict()
somaCarrinho = 0

produtos = {'maça':2.5, 'pera':3}

Estoque = []

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
            
            nome = input("Qual o nome do novo produto: ")
            while len(nome) <= 2:
                print("nome não pode conter menos de 2 caracteres'.")
                nome = input("Favor inserir um nome válido")
            #produto['produto'] = novo_produto
            
            valor = float(input("Qual o preço atualizado? \nR$:"))
            while valor <= 0:
                print("Valor deve ser maior que R$ 0")
                valor = input("Favor inserir valor válido: R$")
            produtos[nome]=valor
            Estoque.append(produto.copy())
        else:
            print("opção ainda não cadastrada")

        print(produtos)


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

                    carrinho = carrinho - produtos[produto]

                    menosCarrinho = input(
                        "Deseja remover mais produtos do carrinho? Digite S para sim ou N para não ")


print('''
_______________
Fim de programa!
_______________
''')
print(carrinho)
