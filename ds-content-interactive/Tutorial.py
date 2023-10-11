import numpy as np
import matplotlib.pyplot as plt

# * `numpy` a biblioteca Python mais popular para manipulação de arrays e computação numérica
# * `matplotlib` a biblioteca de visualização mais popular no ecossistema Python.
# Vamos agora executar algumas linhas de código e gerar alguns gráficos:

x = np.linspace(0, 10, 500)
y = np.cumsum(np.random.randn(500, 6), 0)

plt.figure(figsize=(12, 7))
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')

import requests
import pandas as pd

# Tenho uma função predefinida que simplifica o processo de importação de dados do [Cryptowatch](https://cryptowat.ch) (para referência, consulte [a documentação deles](https://cryptowat.ch/docs/api#ohlc)).

def get_historic_price(symbol, exchange='bitfinex', after='2018-09-01'):
    url = 'https://api.cryptowat.ch/markets/{exchange}/{symbol}usd/ohlc'.format(
        symbol=symbol, exchange=exchange)
    resp = requests.get(url, params={
        'periods': '3600',
        'after': str(int(pd.Timestamp(after).timestamp()))
    })
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data['result']['3600'], columns=[
        'CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume', 'NA'
    ])
    df['CloseTime'] = pd.to_datetime(df['CloseTime'], unit='s')
    df.set_index('CloseTime', inplace=True)
    return df

# Agora vou buscar dados do Bitcoin e Ether, duas das criptomoedas mais populares, para os últimos 7 dias:

last_week = (pd.Timestamp.now() - pd.offsets.Day(7))
last_week

btc = get_historic_price('btc', 'bitstamp', after=last_week)

eth = get_historic_price('eth', 'bitstamp', after=last_week)

# **Bitcoin:**

btc.head()

btc['ClosePrice'].plot(figsize=(15, 7))

# **Ether:**

eth.head()

eth['ClosePrice'].plot(figsize=(15, 7))

# Como você pode ver, somos capazes de buscar dados da internet com apenas algumas linhas, criar um DataFrame e plotá-lo tudo dentro do Jupyter Lab.

eth.head()

from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook

output_notebook()

# E geramos o gráfico:

p1 = figure(x_axis_type="datetime", title="Preços de Cripto", width=800)
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Data'
p1.yaxis.axis_label = 'Preço'

p1.line(btc.index, btc['ClosePrice'], color='#f2a900', legend='Bitcoin')
#p1.line(eth.index, eth['ClosePrice'], color='#A6CEE3', legend='Ether')

p1.legend.location = "top_left"

show(p1)

# ☝️ como você pode ver, o gráfico é interativo. Experimente fazer zoom in e out, e rolar no gráfico.
# Parte 4: Exportando para Excel
# Agora estamos prontos para gerar um arquivo Excel a partir dos preços baixados. Trabalhar com Excel e outros formatos (como CSV ou JSON) é extremamente simples no Jupyter Lab (graças ao pandas e Python). Nosso primeiro passo será criar um "escritor de Excel", um componente do pacote `pandas`:

writer = pd.ExcelWriter('criptos.xlsx')

# Agora vamos escrever nossos dados de Bitcoin e Ether como planilhas separadas:

btc.to_excel(writer, sheet_name='Bitcoin')

eth.to_excel(writer, sheet_name='Ether')

# E finalmente, podemos salvar o arquivo:

writer.save()