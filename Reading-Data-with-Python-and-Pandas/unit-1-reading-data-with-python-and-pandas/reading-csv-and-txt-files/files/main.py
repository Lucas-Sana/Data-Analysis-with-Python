import pandas as pd

# Lê o arquivo CSV especificando o separador, vírgula neste caso
df = pd.read_csv('btc-market-price.csv', sep=',')

# Define o cabeçalho das colunas
df.columns = ['Timestamp', 'Price']

# Lê o arquivo CSV pulando as duas primeiras linhas
df = pd.read_csv('exam_review.csv', sep='>', skiprows=2)

# Lê o arquivo CSV com ponto e vírgula como separador e especifica a codificação
df = pd.read_csv('exam_review.csv', sep=';', encoding='utf-8')

# Lê o arquivo CSV com vírgula como separador e especifica a vírgula como separador decimal
df = pd.read_csv('exam_review.csv', sep='>', decimal=',')

# Lê o arquivo CSV especificando as colunas a serem carregadas
df = pd.read_csv('exam_review.csv', sep='>', usecols=['first_name', 'last_name', 'age'])

# Lê o arquivo CSV e carrega os dados em uma série (uma única coluna)
series = pd.read_csv('exam_review.csv', sep='>', usecols=['last_name'], squeeze=True)

# Salva o DataFrame em um arquivo CSV sem incluir o índice
df.to_csv('out.csv', index=False)
