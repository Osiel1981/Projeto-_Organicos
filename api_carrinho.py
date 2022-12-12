from flask import Flask
from flask import render_template
from flask import url_for, redirect
from flask import request
import pandas as pd
import sqlite3 as sql


#criar banco de dados
conexao = sql.connect('inventory.db')
cursor = conexao.cursor()

#criar tabela
create_table_estoque = '''
CREATE TABLE IF NOT EXISTS estoque(
   produto    TEXT NOT NULL PRIMARY KEY
  ,preco     MONEY NOT NULL
  ,quantidade INT  NOT NULL
);'''

insert_valors_estoque = '''
INSERT INTO mytable(produto,preco,quantidade) VALUES
 ('maça',4,42)
,('pera',3,22)
,('melancia',8,30)
,('queijo',25,60)
,('melao',8,38)
,('manga',8,50)
,('leite',10,70)
,('ovos',10,60)
,('Abacaxi',6,30)
,('agua',2,43)
,('farofa',10,40)
,('goiba',6,50)
,('pitanga',5,45);
'''


cursor.execute(create_table_estoque)
cursor.execute(insert_valors_estoque)

conexao.commit()

app = Flask(__name__)

carrinho = pd.DataFrame(data={
        'produto': [],
        'preco': [],
        'quantidade': []
    }).set_index('produto')

@app.route('/')
def index():
    return redirect(url_for('static', filename='Landing_page.html'))


@app.route('/adicionarCarrinho')
def adicionarCarrinho():
    argumentos = request.args.to_dict()
    produto = argumentos['produto']
    quantidade = argumentos['quantidade']
    preco = estoque.loc[produto,'preco'] # consultar preço do produto escolido e adicinar esse valor a variavel preço 
    carrinho.loc[produto] = [float(preco),int(quantidade)]
    print(carrinho)
    return redirect('static/Carrinho.html')

@app.route('/fecharVenda')
def fecharVenda():
    global carrinho
    for item in carrinho.index:
        estoque.loc[item, 'quantidade'] = int(estoque.loc[item,'quantidade'])-int(carrinho.loc[item,'quantidade']) # criar um query que subitraia a quantidade no banco de dados igual a variavel quantidade
    
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
    print(carrinho),

   
    return render_template('fecharvenda.html', table = df_html)


@app.route('/removerCarrinho')
def removerCarrinho():
    global carrinho

    argumentos = request.args.to_dict()
    produto = argumentos['produto']

    carrinho.drop(index=produto, inplace=True)
    print(carrinho)

    return redirect('/static/removerCarrinho.html')




app.run(debug=True)