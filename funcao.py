from cgitb import html
import pandas as pd

df = pd.read_csv('estoque.csv')
df_html = df.to_html()
lista = open("static/lista.html", "w")
lista.write(df_html)
lista.close()

