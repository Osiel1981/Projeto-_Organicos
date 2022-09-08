from re import A
produtos = {}
vendas = []
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

        preco_produto = float(input("Qual o preço atualizado? \nR$:"))
        while preco_produto <= 0:
            print("Valor deve ser maior que R$ 0")
            input("Favor inserir valor válido: R$")
        produtos = novo_produto,preco_produto

        print("Produto cadastrado, :", novo_produto)
        print(produtos)
    else:
        print("opção ainda não cadastrada")


    


print("Fim de programa")
print ("oi anderson ")