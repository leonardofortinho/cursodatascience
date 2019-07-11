from scipy.stats import t

"""
Média de salário dos cientistas de dados é de R$ 75,00 por hora. Amostra com 9
funcionários e desvio padrão = 10. Qual a probabilidade de selecionar um
cientista de dados e o salário ser menor que R$ 80,00 por hora?
"""

salario_menor = t.cdf(1.5, 8)

"""
Qual a probabilidade do salário ser maior do que 80?
"""

salario_maior = t.sf(1.5, 8) # Forma 1
salario_maior2 = 1 - t.cdf(1.5, 8) # Forma 2

salario_maior_porcentagem = t.sf(1.5, 8) * 100
soma_dois_valores = t.cdf(1.5, 8) + t.sf(1.5, 8)