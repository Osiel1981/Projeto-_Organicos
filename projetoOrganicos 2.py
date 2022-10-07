
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

    produtos[produto] = [preco, quantidade]
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
    carrinho.loc[produto] = [preco,quantidade]
    print(carrinho)
    return redirect('static/Carrinho.html')

#menu vendas
@app.route('/vendas')
def vendas():
    return redirect(url_for('static', filename='vendas.html'))

#exibição de relatorio
@app.route('/relatorio')
def relatorio():
    return redirect(url_for('static', filename='relatorio.html'))

app.run()