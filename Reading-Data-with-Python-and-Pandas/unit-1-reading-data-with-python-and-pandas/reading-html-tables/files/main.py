# Importando a biblioteca pandas
import pandas as pd

# Definindo o conteúdo HTML como uma string
html_string = """
<table>
    <thead>
      <tr>
        <th>Order date</th>
        <th>Region</th> 
        <th>Item</th>
        <th>Units</th>
        <th>Unit cost</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1/6/2018</td>
        <td>East</td> 
        <td>Pencil</td>
        <td>95</td>
        <td>1.99</td>
      </tr>
      <tr>
        <td>1/23/2018</td>
        <td>Central</td> 
        <td>Binder</td>
        <td>50</td>
        <td>19.99</td>
      </tr>
      <tr>
        <td>2/9/2018</td>
        <td>Central</td> 
        <td>Pencil</td>
        <td>36</td>
        <td>4.99</td>
      </tr>
      <tr>
        <td>3/15/2018</td>
        <td>West</td> 
        <td>Pen</td>
        <td>27</td>
        <td>19.99</td>
      </tr>
    </tbody>
</table>
"""

# Lendo o conteúdo HTML em uma lista de DataFrames
dfs = pd.read_html(html_string)

# Selecionando o primeiro DataFrame da lista
df = dfs[0]

# Imprimindo o DataFrame
print(df)

# Lendo dados de uma URL
html_url = "https://www.basketball-reference.com/leagues/NBA_2019_per_game.html"
nba_tables = pd.read_html(html_url)
nba = nba_tables[0]
print(nba.head())

# Importando a biblioteca requests
import requests

# Obtendo o código HTML de uma URL
html_url = "https://en.wikipedia.org/wiki/The_Simpsons"
r = requests.get(html_url)
wiki_tables = pd.read_html(r.text, header=0)

# Selecionando o segundo DataFrame da lista
simpsons = wiki_tables[1]
print(simpsons.head())

# Limpando o DataFrame simpsons
simpsons.drop([0, 1], inplace=True)
simpsons.set_index('Season', inplace=True)

# Encontrando a temporada com o menor número de episódios
min_season = simpsons['No. ofepisodes'].min()
min_season_df = simpsons.loc[simpsons['No. ofepisodes'] == min_season]
print(min_season_df)

# Salvando o DataFrame como um arquivo CSV
simpsons.to_csv('out.csv')
