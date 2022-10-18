'''from cgitb import html
from flask import render_template
import pandas as pd
from flask import Flask

app = Flask(__name__)
@app.route('/')
def listar():
    df = pd.read_csv('estoque.csv')
    df_html = df.to_html()
    print(df_html)
    return render_template('lista.html', table = df_html)
app.run()

'''