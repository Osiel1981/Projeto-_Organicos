
# Aqui estão as variáveis do programa
from turtle import clear
import os

menunavegacao = '''
------------------------
    Menu de navegação

[C] Cadastro
[V] Vendas 
[R] Relatórios
[S] Encerrar o programa
------------------------'''

menucadastro = '''
-------------------------------
       Menu de Cadastro

[C] Produtos a cadastrar
[L] Listar produtos cadastrados 
[D] Deleção de produtos
[V] Voltar para o menu principal
[S] Sair do programa
-------------------------------'''

menu_vendas = '''
-------------------------------
        Menu de Vendas
            
[A] Adicionar item ao carrinho
[R] Remover item do carrinho
[F] Fechar e finalizar a compra
[C] Ver os items do carrinho
[V] Voltar para o menu inicial
-------------------------------
'''

menu_relatorio = '''
------------------------------
      Menu de Relatorio

[E] Exibir Relatorio
[V] Voltar para o menu inicial
[S] Sair do programa
------------------------------'''
faturamento = 0
numero_de_vendas = 0
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
print('=' * 30),print(' ' * 30),print ('''Desenvolvedores:             
                                                     
            Anderson Teixeira  
            Eron Morais        
            João Paulo Garcia  
            Osiel Mesquita     '''),print(' ' * 30),print('=' * 30)
print(' ' * 30)

opcao = "a"
while opcao.upper() != "S":
    print(menunavegacao)
    opcao = input("Digite o que deseja acessar: \n").upper()
    os.system('cls')
    if opcao.upper() == 'C': # Menu de cadastro
        opcaocadastro = 'C'

        while opcaocadastro.upper() in "CLDP":
            print(menucadastro)
            opcaocadastro = input("Digite o que deseja acessar: \n").upper()
            if opcaocadastro == 'C':
                while opcaocadastro == "C":   
                    nome = input("Qual o nome do novo produto: \n").lower()
                    while len(nome) <= 2:
                        print("Nome não pode conter menos de 2 caracteres'.")
                        nome = input("Favor inserir um nome válido:\n").lower()
                    
                    valor = float(input("Qual o preço atualizado? \nR$ "))
                    while valor <= 0:
                        print("Valor deve ser maior que R$ 0")
                        valor = float(input("Favor inserir valor válido: \nR$"))
                    if nome in produtos:
                        input(f'''
                    Produto {nome} já cadastrado.
                    O valor será atualizado para R$:{valor}.''')
                        produtos[nome]=valor

                    else:
                        produtos[nome]=valor

                    opcaocadastro = input("Deseja cadastrar novo produto? \nS - Sim *** N - Menu anterior *** Q - Menu principal \n").upper()
                    os.system('cls')
                    if opcaocadastro == 'S':
                        opcaocadastro = 'C'
                    if opcaocadastro == 'N':
                        opcaocadastro = 'P'
                    if opcaocadastro == 'V':
                        opcao = 'Q'
                    
            if opcaocadastro == 'L':
                for items in produtos:
                    print(f'{items:<20s} {str(produtos[items]):>} ')
                    
            if opcaocadastro == 'D':
                menosproduto = 'S'
                os.system('cls')
                while menosproduto == 'S':
                    produto = input("Digite o produto que deseja excluir:\n").lower()
                    if produto in produtos.keys():
                        produtos.pop(produto)
                    else:
                        print('''
                            --------------------------------------
                                Produto indisponível no estoque
                            --------------------------------------
                            ''')
                    menosproduto = input("Deseja remover mais produtos? \nDigite S para Sim ou N para Não \n").upper()
                    os.system('cls')
            if opcaocadastro == 'V':
                        opcao = 'Q'
                        os.system('cls')
            if opcaocadastro == 'S':
                opcao = 'S'
        

    if opcao.upper() == "V": # Menu de vendas 
        opcaoVendas = "A"
        while opcaoVendas.upper() in "ARFC":
            print(menu_vendas)
            opcaoVendas = input("Digite o que deseja acessar: \n")

            if opcaoVendas.upper() == "A":
                maisCarrinho = "S"

                while maisCarrinho.upper() == "S":
                    produto = input("Digite o produto a ser adicionado ao carrinho: ")

                    if produto in carrinho.keys():
                            valor = carrinho[produto] + produtos[produto]
                            carrinho[produto] = valor

                    elif produto in produtos.keys():

                            valor = produtos[produto]
                            carrinho[produto] = valor


                    else:
                        print('''
                        ------------------------
                        Esse produto não cadastrado!
                        ------------------------
                        ''')

                    maisCarrinho = input("Deseja adicionar mais produtos ao carrinho? Digite S para sim ou N para não: ")
                    os.system('cls')
            if opcaoVendas.upper() == "R":
                menosCarrinho = "S"
                while menosCarrinho.upper() == "S":
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
                    os.system('cls')
            if opcaoVendas.upper() == "F":
                for nomes in carrinho:
                    valores = carrinho[nomes]
                    somaCarrinho = somaCarrinho + valores
                print(f'''
                ++++++++++++++++++++++++++++++++++++++
                          Itens no Carrinho
                             {carrinho}
                ++++++++++++++++++++++++++++++++++++++
                Valor total a pagar = R${somaCarrinho}
                ++++++++++++++++++++++++++++++++++++++''')
                faturamento = faturamento + somaCarrinho
                vendidos.update(carrinho)
                carrinho.clear()
                somaCarrinho = 0
                numero_de_vendas = numero_de_vendas + 1

            if opcaoVendas.upper() == "C":
                print(f'''
                +++++++++++++++++++++
                     Seu Carrinho
                +++++++++++++++++++++
                {carrinho}
                +++++++++++++++++++++''')

    if opcao.upper() == 'R': # Menu de Relatorio
        opcaorelatorio = 'R'

        while opcaorelatorio.upper() in "CR":
            print(menu_relatorio)

            opcaorelatorio = input("Digite o que deseja acessar: \n").upper()
            if opcaorelatorio == 'E':
                if numero_de_vendas > 0:
                    for items in vendidos:
                        print(' ' * 1),
                        print(f'Itens Vendidos'),
                        print(' ' * 1),
                        print(f'|{items:<10s}'),
                        print(' ' * 1),
                    print(f'Hoje foram feitas {numero_de_vendas} vendas'),
                    print(f'O faturamento Diario foi R$ : {round(faturamento,2)}'),                    
                    print(f'O ticket medio do dia de hoje foi : {round(faturamento/numero_de_vendas,2)}'),
                else:
                    print("Não há vendas registradas")

print('''
_______________
Fim de programa!
_______________
''')
