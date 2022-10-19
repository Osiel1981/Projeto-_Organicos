
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
    return redirect(url_for('static', filename='Landing_page.html'))

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

    estoque.loc[produto]= [preco,quantidade]
    estoque.to_csv('estoque.csv')
    print(estoque)

    return redirect('static\cadastro.html')

@app.route('/excluirProduto')
def excluirProduto():
    estoque = pd.read_csv('estoque.csv', index_col='produto')

    argumentos = request.args.to_dict()
    produto = argumentos['produto']

    estoque.drop(index=produto, inplace=True)
    print(estoque)
    estoque.to_csv('estoque.csv')

    return redirect('/static/removerEstoque2.html')
    

#função para mostrar no dataframe de estoque, sera usado para mostrar todos os itens do estoque 
@app.route('/lista')
def listar():
    df = pd.read_csv('estoque.csv')
    df_html = df.to_html()
    return render_template('lista.html', table = df_html)

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
    df_html = carrinho.to_html()
    carrinho = pd.DataFrame(data={
            'produto': [],
            'preco': [],
            'quantidade': []
        }).set_index('produto')
    print(carrinho)
    
    return render_template('fecharvenda.html', table = df_html)

@app.route('/removerCarrinho')
def removerCarrinho():
    global carrinho

    argumentos = request.args.to_dict()
    produto = argumentos['produto']

    carrinho.drop(index=produto, inplace=True)
    print(carrinho)

    return redirect('/static/removerCarrinho.html')

#exibição de relatorio
@app.route('/relatorio')
def relatorio():
    return redirect(url_for('static', filename='relatorio.html'))

@app.route('/listar/carrinho')
def listarCarrinho():
    df = carrinho
    df_html = df.to_html()
    return render_template('carrinho.html', table = df_html)

app.run(debug=True)