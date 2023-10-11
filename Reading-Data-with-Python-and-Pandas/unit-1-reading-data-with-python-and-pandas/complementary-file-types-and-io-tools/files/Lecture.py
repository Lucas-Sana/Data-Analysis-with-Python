import pandas as pd

# Criando um DataFrame
df = pd.DataFrame([[1,2,3], [4,5,6]],
                  columns=['A','B','C'])

# Exibindo o DataFrame
print(df)

# Salvando o DataFrame em um arquivo pickle
df.to_pickle('out.pkl')

# Lendo o conteúdo do arquivo pickle
with open('out.pkl', 'rb') as file:
    content = file.read()
    print(content)

# Lendo o DataFrame de volta do arquivo pickle
df = pd.read_pickle('out.pkl')
print(df)

# Lendo dados da área de transferência
df = pd.read_clipboard()
print(df)

# Escrevendo dados na área de transferência
df.to_clipboard()
print(pd.read_clipboard())

# Lendo um arquivo SAS
df = pd.read_sas('airline.sas7bdat')
print(df.head())

# Lendo um arquivo SAS de uma URL
sas_url = 'http://www.principlesofeconometrics.com/sas/airline.sas7bdat'
df = pd.read_sas(sas_url)
print(df.head())
print(df.loc[:,'Y'].plot())

# Lendo um arquivo STATA
df = pd.read_stata('broiler.dta')
print(df.head())

# Lendo um arquivo STATA de uma URL
stata_url = 'http://www.principlesofeconometrics.com/stata/broiler.dta'
df = pd.read_stata(stata_url)
print(df.head())
print(df.loc[:,'cpi'].plot())

# Lendo dados do Google BigQuery (requer pandas-gbq)
import pandas_gbq

sql = """
    SELECT name, SUM(number) as count
    FROM `bigquery-public-data.usa_names.usa_1910_current`
    GROUP BY name
    ORDER BY count DESC
    LIMIT 10
"""

df_gbq = pandas_gbq.read_gbq(sql, project_id='MY_PROJECT_ID')
print(df_gbq)
