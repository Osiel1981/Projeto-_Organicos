
# Aqui estão as variáveis do programa
from turtle import clear
menunavegacao = '''
    -----------------------
    Menu de navegação
    C = cadastro
    V = vendas 
    R = Relatórios
    S = Encerrar o programa
    -----------------------'''

menucadastro = '''
    -----------------
Menu de Cadastro
P = Produtos a cadastrar
L = Listar produtos cadastrados 
D = Deleção de produtos
V = Voltar para o menu anterior
S = Sair do programa
    -----------------'''

carrinho = {}
somaCarrinho = 0
produtos = {'maça':2.5, 'pera':3}
vendidos = {}
preco = 0


print('=' * 30),print('-' * 30),print(' ' * 30),print('\\' * 30), print('BEM VINDO AO DESAFIO PYTHON #1' )
print('//' * 15)
print(' ' * 15),
print('-' * 30),print('=' * 30),print ('Orientação :   Matheus Willian'),print('=' * 30)
print('''
          .-------.             
         _|_O_    |_            
        |         | |           
        | .-------' |           
        |_|    _____|           
          |     O |           
          '-------' ''')
print(''' ''')
print('=' * 30),print(' ' * 30),print ('''Desnvolvedores:             
                                                     
            Anderson Teixeira  
            Eron Morais        
            João Paulo Garcia  
            Osiel Mesquita     '''),print(' ' * 30),print('=' * 30)
print(' ' * 30)

opcao = "a"
while opcao.upper() != "S":
    print(menunavegacao)

    opcao = input("Digite o que deseja acessar: \n").upper()
    
    if opcao.upper() == 'C': # Menu de cadastro
        opcaocadastro = 'C'

        while opcaocadastro.upper() in "CLD":
            print(menucadastro)

            opcaocadastro = input("Digite o que deseja acessar: \n").upper()
            if opcaocadastro == 'P':
                while opcaocadastro == "P":   
                    nome = input("Qual o nome do novo produto: \n").lower()
                    while len(nome) <= 2:
                        print("Nome não pode conter menos de 2 caracteres'.")
                        nome = input("Favor inserir um nome válido:\n").lower()
                    
                    valor = float(input("Qual o preço atualizado? \nR$: \n"))
                    while valor <= 0:
                        print("Valor deve ser maior que R$ 0")
                        valor = input("Favor inserir valor válido: \nR$")
                    produtos[nome]=valor

                    opcaocadastro = input("Deseja cadastrar novo produto? \nS - Sim *** N - Menu anterior *** Q - Menu principal \n").upper()
                    if opcaocadastro == 'S':
                        opcaocadastro = 'P'
                    if opcaocadastro == 'N':
                        opcaocadastro = 'C'
                    if opcaocadastro == 'V':
                        opcao = 'Q'
                    
            if opcaocadastro == 'L':
                for items in produtos:
                    print(f'{items:<20s} {str(produtos[items]):>} ')
            if opcaocadastro == 'D':
                menosproduto = 'S'
                while menosproduto == 'S':
                    produto = input("Digite o produto que deseja excluir!\n").lower()
                    if produto in produtos.keys():
                        produtos.pop(produto)
                    else:
                        print('''
                            --------------------------------------
                                Produto indisponível no estoque
                            --------------------------------------
                            ''')
                    menosproduto = input("Deseja remover mais produtos do carrinho? Digite S para Sim ou N para Não \n").upper()

            if opcaocadastro == 'V':
                        opcao = 'Q'
            if opcaocadastro == 'S':
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
            Digite S para voltar para o menu inicial: 
              
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
                vendidos.update(carrinho)
                carrinho.clear()
                somaCarrinho = 0

            if opcaoVendas.upper() == "C":
                
                print(f'''
                +++++++++++++++++++++
                Itens no Carrinho
                +++++++++++++++++++++
                {carrinho}
                +++++++++++++++++++++''')
    if opcao.upper() == 'R': # Menu de Relatorio
        opcaorelatorio = 'R'

        while opcaorelatorio.upper() in "CVR":
            print('''
    -----------------
    Menu de Relatorio
    E = Exibir Relatorio
    V = Voltar para o menu anterior
    S = Sair do programa
    -----------------''')

            opcaorelatorio = input("Digite o que deseja acessar: ").upper()
            if opcaorelatorio == 'E':
                    for items in produtos:
                        print(' ' * 1),
                        print(f'|{items:<10s}|{str(produtos[items]):>10s}|')

print('''
_______________
Fim de programa!
_______________
''')
