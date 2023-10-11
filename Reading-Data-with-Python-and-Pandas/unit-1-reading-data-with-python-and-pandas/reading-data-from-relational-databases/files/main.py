import sqlite3
import pandas as pd
from sqlalchemy import create_engine

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('chinook.db')

# Cria um cursor para executar comandos SQL
cur = conn.cursor()

# Executa um comando SQL para buscar as 5 primeiras linhas da tabela employees
cur.execute('SELECT * FROM employees LIMIT 5;')
results = cur.fetchall()

# Cria um DataFrame a partir dos resultados da consulta SQL
df = pd.DataFrame(results)

# Fecha o cursor e a conexão
cur.close()
conn.close()

# Conecta ao banco de dados SQLite novamente
conn = sqlite3.connect('chinook.db')

# Lê os dados da tabela employees diretamente em um DataFrame
df = pd.read_sql('SELECT * FROM employees;', conn)

# Define EmployeeId como índice e faz o parse das colunas BirthDate e HireDate como datas
df = pd.read_sql('SELECT * FROM employees;', conn,
                 index_col='EmployeeId',
                 parse_dates=['BirthDate', 'HireDate'])

# Cria uma conexão com a engine SQLite usando SQLAlchemy
engine = create_engine('sqlite:///chinook.db')
connection = engine.connect()

# Lê os dados da tabela employees diretamente em um DataFrame usando SQLAlchemy
df = pd.read_sql_table('employees', con=connection)

# Define EmployeeId como índice e faz o parse das colunas BirthDate e HireDate como datas
df = pd.read_sql_table('employees', con=connection,
                       index_col='EmployeeId',
                       parse_dates=['BirthDate', 'HireDate'])

# Fecha a conexão
connection.close()

# Conecta ao banco de dados SQLite novamente
conn = sqlite3.connect('chinook.db')

# Cria uma nova tabela employees2 com os dados do DataFrame df
df.to_sql('employees2', conn)

# Lê os dados da tabela employees2
pd.read_sql_query('SELECT * FROM employees2;', conn).head()

# Substitui a tabela employees2 pelo DataFrame df
pd.DataFrame().to_sql('employees2',
                      conn,
                      if_exists='replace')

# Lê os dados atualizados da tabela employees2
pd.read_sql_query('SELECT * FROM employees2;', conn).head()

# Fecha a conexão
conn.close()
