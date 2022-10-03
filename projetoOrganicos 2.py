
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
    return redirect(url_for('static', filename='index.html'))

#menu cadastro
@app.route('/cadastro')
def cadastro():
    return redirect(url_for('static', filename='cadastro.html'))

#menu vendas
@app.route('/vendas')
def vendas():
    return redirect(url_for('static', filename='vendas.html'))

#exibição de relatorio
@app.route('/relatorio')
def relatorio():
    return redirect(url_for('static', filename='relatorio.html'))

app.run()