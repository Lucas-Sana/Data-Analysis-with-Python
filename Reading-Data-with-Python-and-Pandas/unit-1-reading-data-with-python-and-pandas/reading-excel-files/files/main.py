import pandas as pd

# Lê o arquivo Excel "products.xlsx" com a primeira planilha padrão
products = pd.read_excel('products.xlsx', index_col='product_id')

# Lê a planilha "Merchants" do arquivo Excel "products.xlsx" com o "merchant_id" como índice
merchants = pd.read_excel('products.xlsx', sheet_name='Merchants', index_col='merchant_id')

# Cria um arquivo Excel chamado "out.xlsx" e insere o DataFrame "products" na planilha "Products"
products.to_excel('out.xlsx', sheet_name='Products')

# Insere o DataFrame "merchants" na planilha "Merchants" no mesmo arquivo "out.xlsx"
merchants.to_excel('out.xlsx', sheet_name='Merchants')

# Define uma posição específica (linha e coluna) para inserir o DataFrame "products" no arquivo "out.xlsx"
products.to_excel('out.xlsx', sheet_name='Products', startrow=1, startcol=2)

# Salva múltiplas planilhas (DataFrames) no arquivo Excel "out.xlsx" usando um objeto ExcelWriter
with pd.ExcelWriter('out.xlsx') as writer:
    products.to_excel(writer, sheet_name='Products')
    merchants.to_excel(writer, sheet_name='Merchants')
