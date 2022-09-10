
from re import A

carrinho = {}

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

    opcao = input("Digite o que deseja acessar: ").upper()
    if opcao.upper() == 'C': # Menu de cadastro 
        print('''
    -----------------
    Menu de Cadastro
    C = Cadastramento de produtos
    L = Listar produtos cadastrados 
    D = Deleção de produtos
    V = Voltar para o menu anterior
    S = Sair do programa
    -----------------''')

        opcao= input("Digite o que deseja acessar: ").upper()
        if opcao == 'C':
            while opcao == "C":
                nome = input("Qual o nome do novo produto: ").upper()
                while len(nome) <= 2:
                    print("nome não pode conter menos de 2 caracteres'.").upper()
                    nome = input("Favor inserir um nome válido").upper
                
                valor = float(input("Qual o preço atualizado? \nR$:"))
                while valor <= 0:
                    print("Valor deve ser maior que R$ 0")
                    valor = input("Favor inserir valor válido: R$")
                produtos[nome]=valor

                opcao = input("Deseja cadastrar novo produto? S - Sim e N - não! \n").upper()
                if opcao == 'S':
                    opcao = 'C'
        if opcao == 'L':
            print(list(produtos))
        if opcao == 'D':
            print("Opção em construção")
        if opcao == 'V':
            opcao = 'C'
        if opcao== 'S':
            opcao = 'S'

    if opcao.upper() == "V": # Menu de vendas 
        opcaoVendas = "V"
        while opcaoVendas.upper() in "VARFC":

            print('''
        ---------------------------
            Bem Vindo ao Menu de Vendas
        ---------------------------
            ''')
        opcaoVendas = input('''
        Digite A se deseja adicionar um item ao seu carrinho de compras:
        Digite R se deseja remover um item do seu carrinho de compras:
        Digite F para fechar o carrinho e finalizar a compra:
        Digite C para ver os items dentro do carrinho:
        Digite S para voltar para o menu inicil: 
            
        ''')

        if opcaoVendas.upper() == "A":
            maisCarrinho = "S"

            while maisCarrinho.upper() == "S":
                produto = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
                if produto in produtos.keys():

                    valor = produtos[produto]
                    carrinho[produto] = valor

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
                if produto in carrinho.keys():
                    carrinho.pop(produto)

                else:
                    print('''
                    -------------------------------------
                    Esse produto não esta no seu carrinho
                    -------------------------------------
                    ''')
                menosCarrinho = input("Deseja remover mais produtos do carrinho? Digite S para sim ou N para não ")

        if opcaoVendas.upper() == "F":
            for nomes in carrinho:
                valores = carrinho[nomes]
                somaCarrinho = somaCarrinho + valores
            print(f'''
            ++++++++++++++++++++++++++++++++++++++
                        Intens no Carrinho
            {carrinho}
            ++++++++++++++++++++++++++++++++++++++
            Valor total a pagar = R${somaCarrinho}
            ++++++++++++++++++++++++++++++++++++++''')

        if opcaoVendas.upper() == "C":
            
            print(f'''
            +++++++++++++++++++++
            Itens no Carrinho
            +++++++++++++++++++++
            {carrinho}
            +++++++++++++++++++++''')


print('''
_______________
Fim de programa!
_______________
''')

