import pandas as pd

# Carregando os dados do CSV
dados = pd.read_csv('docs/ativos_historico.csv', index_col=0)

# Calculando retorno esperado e volatilidade (risco)
retornos = dados.pct_change().mean() * 252  # Retorno anualizado
risco = dados.pct_change().std() * (252 ** 0.5)  # Volatilidade anualizada

# Salvando as métricas calculadas
metrics = pd.DataFrame({'Retorno Esperado': retornos, 'Risco': risco})
metrics.to_csv('docs/ativos_metricas.csv')