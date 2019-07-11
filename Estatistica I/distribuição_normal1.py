from scipy.stats import norm

"""
Conjunto de objetos em uma cesta, a média é 8 e o desvio padrá é 2. Qual a 
probabilidade de tirar um objeto de peso menor que 6 quilos?
"""
menor_6kg = norm.cdf(6, 8, 2) #Se precisa chamar um valor menor, usar a função 'cdf'

"""
Qual a probabilidade de tirar um objeto que pesa mais que 6 quilos?
"""
mais_6kg = norm.sf(6, 8, 2) #Se precisa chamar um valor maior, usar a função 'sf'
#Forma 2 para obeter o mesmo resultado
mais_6kg_2 = 1 - norm.cdf(6, 8, 2)

"""
Qual a probabilidade de tirar um objeto com o peso menor que 6 ou maior que 
10 quilos?
"""
objeto_menor6g_ou_maior10kg = norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)

"""
Qual a probabilidade de tirar um objeto que pesa menos que 10 quilos e mais 
que 8 quilos?
"""
objeto_menor10kg_ou_maior8kg = norm.cdf(10, 8, 2) - norm.cdf(8, 8, 2)