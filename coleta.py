import os
import yfinance as yf
import pandas as pd

# Criar a pasta docs se não existir
if not os.path.exists('docs'):
    os.makedirs('docs')

# Definindo os ativos financeiros
ativos = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

# Coletando dados do Yahoo Finance
dados = yf.download(ativos, start='2020-01-01', end='2023-01-01')['Adj Close']

# Salvando os dados em um arquivo CSV
dados.to_csv('docs/ativos_historico.csv')