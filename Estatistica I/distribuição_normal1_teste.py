from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

dados = norm.rvs(size = 100) # O 'size' é o tamanho da lista de dados
stats.probplot(dados, plot = plt) # Mostra o gráfico, com a linha

stats.shapiro(dados)