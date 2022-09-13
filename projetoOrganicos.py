from optparse import Values
from os import sep
from re import A
from tkinter import END
from typing import ItemsView
import pprint

carrinho = {}

somaCarrinho = 0

produtos = {'maça':2.5, 'pera':3}

Estoque = []

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
    print('''
    -----------------------
    Menu de navegação
    C = cadastro
    V = vendas 
    R = Relatórios
    S = Encerrar o programa
    -----------------------''')

    opcao = input("Digite o que deseja acessar: ").upper()
    
    if opcao.upper() == 'C': # Menu de cadastro
        opcaocadastro = 'C'

        while opcaocadastro.upper() in "CLD":
            print('''
    -----------------
    Menu de Cadastro
    P = Produtos a cadastrar
    L = Listar produtos cadastrados 
    D = Deleção de produtos
    V = Voltar para o menu anterior
    S = Sair do programa
    -----------------''')

            opcaocadastro = input("Digite o que deseja acessar: ").upper()
            if opcaocadastro == 'P':
                while opcaocadastro == "P":   
                    nome = input("Qual o nome do novo produto: ").lower()
                    while len(nome) <= 2:
                        print("Nome não pode conter menos de 2 caracteres'.")
                        nome = input("Favor inserir um nome válido").lower()
                    #produto['produto'] = novo_produto
                    
                    valor = float(input("Qual o preço atualizado? \nR$:"))
                    while valor <= 0:
                        print("Valor deve ser maior que R$ 0")
                        valor = input("Favor inserir valor válido: R$")
                    produtos[nome]=valor

                    opcaocadastro = input("Deseja cadastrar novo produto? \nS - Sim *** N - Menu anterior *** Q - Menu principal \n").upper()
                    if opcaocadastro == 'S':
                        opcaocadastro = 'P'
                    if opcaocadastro == 'N':
                        opcaocadastro = 'C'
                    if opcaocadastro == 'Q':
                        opcao = 'Q'
                    if opcaocadastro == 'V':
                        opcao = 'Q'
                    
            if opcaocadastro == 'L':
                for items in produtos:
                    print(f'{items} {str(produtos[items]):>20s}')
            if opcaocadastro == 'D':
                menosproduto = 'S'
                while menosproduto == 'S':
                    produto = input("Digite o produto que deseja excluir!").lower()
                    if produto in produtos.keys():
                        produtos.pop(produto)
                    else:
                        print('''
                            --------------------------------------
                                Produto indisponível no estoque
                            --------------------------------------
                            ''')
                    menosproduto = input("Deseja remover mais produtos do carrinho? Digite S para Sim ou N para Não ").upper()

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