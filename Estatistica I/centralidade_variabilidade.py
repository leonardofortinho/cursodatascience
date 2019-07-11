import numpy as np
from scipy import stats

jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]
media = np.mean(jogadores)
mediana = np.median(jogadores)

quartis = np.quantile(jogadores, [0, 0.25, 0.5, 0.75, 1])
desvio_padrao = np.std(jogadores, ddof = 1) 
# aqui tem que adicionar o 'ddof = 1' para ele fazer o calculo igual ao R

stats.describe(jogadores)