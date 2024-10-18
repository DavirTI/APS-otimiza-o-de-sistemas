import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando dados de métricas e alocação
metrics = pd.read_csv('docs/ativos_metricas.csv', index_col=0)
alocacao = pd.read_csv('docs/ativos_alocacao.csv', index_col=0).squeeze("columns")

# Fronteira eficiente
plt.figure(figsize=(10, 6))
sns.scatterplot(x=metrics['Risco'], y=metrics['Retorno Esperado'], s=100)
plt.xlabel('Risco (Volatilidade)')
plt.ylabel('Retorno Esperado')
plt.title('Fronteira Eficiente')
plt.savefig('docs/fronteira_eficiente.png')
plt.show()

# Gráfico de alocação de ativos
plt.figure(figsize=(8, 8))
plt.pie(alocacao, labels=metrics.index, autopct='%1.1f%%')
plt.title('Alocação de Ativos')
plt.savefig('docs/alocacao_ativos.png')
plt.show()
