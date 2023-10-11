# Importando a biblioteca pandas
import pandas as pd

# Lendo um arquivo JSON em um DataFrame
games = pd.read_json('games.json')

# Visualizando as primeiras linhas do DataFrame
print(games.head())

# Lendo um arquivo JSON com estrutura aninhada
import json

with open('users.json') as file:
    json_dict = json.load(file)

# Convertendo o dicionário aninhado em um DataFrame
df = pd.DataFrame.from_dict(json_dict['info'])

# Visualizando as primeiras linhas do DataFrame
print(df.head())

# Usando json_normalize para tratar colunas aninhadas
from pandas.io.json import json_normalize

# Descompactando a coluna "address" em um novo DataFrame
address = json_normalize(json_dict['info'], sep='_', record_path='address')

# Visualizando as primeiras linhas do DataFrame
print(address.head())

# Salvando um DataFrame como um arquivo JSON
users.to_json('out.json')

# Lendo o arquivo JSON recém-salvo
pd.read_json('out.json').head()