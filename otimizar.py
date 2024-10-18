import pandas as pd
from scipy.optimize import linprog

# Carregando métricas dos ativos
metrics = pd.read_csv('docs/ativos_metricas.csv', index_col=0)
retornos = metrics['Retorno Esperado']
risco = metrics['Risco']

# Definindo a capacidade da mochila (limite de risco máximo)
R = 0.5  # Aumentando a tolerância de risco

# Definindo a função objetivo (retorno negativo para maximização)
c = -retornos.values

# Restrições
A = [risco.values]  # Matriz de coeficientes (risco de cada ativo)
b = [R]  # Capacidade (risco máximo permitido)

# Restrições de que x_i deve ser entre 5% e 40% (proporção de investimento)
bounds = [(0.05, 0.4) for _ in range(len(retornos))]  # Máximo de 40%, mínimo de 5% por ativo

# Resolvendo o problema de otimização
resultado = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# Mostrando a alocação final
alocacao = pd.Series(resultado.x, index=metrics.index)
alocacao.to_csv('docs/ativos_alocacao.csv')

# Exibindo os pesos otimizados para ver a distribuição
print("Alocação Otimizada:", alocacao)