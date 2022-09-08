
print('''
==================================
Bem Vindo ao Desefio Organicos!!!
==================================
''')

opcao = "a"
while opcao.upper() != "S": 
    print('''
    -----------------
    Menu de navegação
    -----------------
    C = cadastro
    V = vendas 
    R = Relatórios
    S = sair e feixar o programa
    -----------------
    ''')

    opcao = input("Digite o que deseja acessar: ")
    if not opcao.upper() in "CVRS": 
        print('''
        _______________
        OPÇÃO INVALIDA
        _______________''')


print('''
_______________
Fim de programa!
_______________
''')
