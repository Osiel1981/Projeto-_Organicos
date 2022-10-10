
from fileinput import filename
from multiprocessing.sharedctypes import Value
from optparse import Values
from flask import Flask
from flask import render_template
from flask import url_for, redirect
from flask import request
import pandas as pd


app = Flask(__name__)

produtos_lista = []
precos = []
quantidades = []
produtos = {} 

'''estoque = pd.DataFrame(data={
        'produto': [],
        'preco': [],
        'quantidade': []
    }).set_index('produto')'''

carrinho = pd.DataFrame(data={
        'produto': [],
        'preco': [],
        'quantidade': []
    }).set_index('produto')

estoque = pd.read_csv('estoque.csv', index_col='produto')

#menu principal
@app.route('/')
def index():
    return redirect(url_for('static', filename='index2.html'))

#menu cadastro
@app.route('/cadastro')
def cadastro():
    return redirect(url_for('static', filename='cadastro.html'))

#cadastrar novos produtos
@app.route('/cadastrarProdutos')
def cadastrarProdutos():
    
    argumentos = request.args.to_dict()
    produto = argumentos['produto']
    preco = argumentos['preco']
    quantidade = argumentos['quantidade']

    produtos_lista.append(produto)
    precos.append(preco)
    quantidades.append(quantidade)

    produtos[produto] = [float(preco), int(quantidade)]
    print(estoque)

    estoque.loc[produto]= [preco,quantidade]
    estoque.to_csv('estoque.csv')
    return redirect('static/formulario.html')

#função para mostrar no dataframe de estoque, sera usado para mostrar todos os itens do estoque 
@app.route('/listaEstoque')
def ListaEstoque():
    return estoque

#adicionar itens ao carrinho, carrinho nao precisa ser salvo em csv pois sera deletado depois de finalizar a compra 
@app.route('/adicionarCarrinho')
def adicionarCarrinho():
    argumentos = request.args.to_dict()
    produto = argumentos['produto']
    quantidade = argumentos['quantidade']
    preco = estoque.loc[produto,'preco']
    carrinho.loc[produto] = [float(preco),int(quantidade)]
    print(carrinho)
    estoque.loc[produto] = [preco,int(estoque.loc[produto,'quantidade'])-int(quantidade)]
    print(estoque)
    return redirect('static/Carrinho.html')

#menu fechar carrinho, precisa dar o valor total da venda, mostrar o carrinho, subitrair a quantidade do estoque e zerar o carrinho
@app.route('/fecharVenda')
def fecharVenda():
    global carrinho
    for item in carrinho.index:
        estoque.loc[item, 'quantidade'] = int(estoque.loc[item,'quantidade'])-int(carrinho.loc[item,'quantidade'])
    
    carrinho['total'] = carrinho['quantidade']*carrinho['preco']
    
    print(carrinho)
    print('__________________________')
    print(carrinho['total'])# item vendidos 
    print(carrinho['total'].sum())# valor total da venda
    print('________________________')
    print(estoque)

    carrinho = pd.DataFrame(data={
            'produto': [],
            'preco': [],
            'quantidade': []
        }).set_index('produto')
    print(carrinho)
    return redirect('/static/index2.html')

def vendas():
    return redirect(url_for('static', filename='vendas.html'))

#exibição de relatorio
@app.route('/relatorio')
def relatorio():
    return redirect(url_for('static', filename='relatorio.html'))

app.run()