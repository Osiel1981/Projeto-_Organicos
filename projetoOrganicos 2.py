
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

'''df = pd.DataFrame(data={
        'produto': [],
        'preco': [],
        'quantidade': []
    }).set_index('produto')'''

df = pd.read_csv('estoque.csv', index_col='produto')

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
    print(df)

    df.loc[produto]= [preco,quantidade]
    df.to_csv('estoque.csv')
    return redirect('static/formulario.html')


#menu vendas
@app.route('/vendas')
def vendas():
    return redirect(url_for('static', filename='vendas.html'))

#exibição de relatorio
@app.route('/relatorio')
def relatorio():
    return redirect(url_for('static', filename='relatorio.html'))

app.run()