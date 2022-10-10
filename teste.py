from wsgiref.validate import validator
import pandas as pd

df = pd.read_csv('estoque.csv', index_col='produto')

valor = df.loc['banana','preco']
print(valor)