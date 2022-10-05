
from fileinput import filename
from multiprocessing.sharedctypes import Value
from optparse import Values
from flask import Flask
from flask import render_template
from flask import url_for, redirect
from flask import request
import pandas as pd
import numpy as np

app = Flask(__name__)

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
    df = pd.read_csv('C:/Users/jop_garcia/Documents/Projeto-_Organicos-1/bancos de dados/bancoDeProdutos.csv', index_col=['produto'])

    argumentos = request.args.to_dict()
    produto = argumentos['produto']
    preco = argumentos['preco']
    quantidade = argumentos['quantidade']

    df.loc[produto]= [preco,quantidade]
    df.to_csv('C:/Users/jop_garcia/Documents/Projeto-_Organicos-1/bancos de dados/bancoDeProdutos.csv')
    return redirect(url_for('static', filename= 'formulario.html'))


#menu vendas
@app.route('/vendas')
def vendas():
    return redirect(url_for('static', filename='vendas.html'))

#exibição de relatorio
@app.route('/relatorio')
def relatorio():
    return redirect(url_for('static', filename='relatorio.html'))

app.run()