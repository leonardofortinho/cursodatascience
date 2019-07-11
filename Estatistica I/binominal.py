from scipy.stats import binom

"""
Jogar uma moeda 5 vezes, qual a probilidade de dar cara 3 vezes.
"""
prodb = binom.pmf(3,5,0.5)

"""
Passar por 4 sinais de 4 tempos, qual a probilidade de pegar sinal verde
Nenhuma, 1, 2, 3 ou 4 vezes seguidas?
"""
nenhum = binom.pmf(0, 4, 0.25)
verde1 = binom.pmf(1, 4, 0.25)
verde2 = binom.pmf(2, 4, 0.25)
verde3 = binom.pmf(3, 4, 0.25)
verde4 = binom.pmf(4, 4, 0.25)


# E se forem de dois tempos?
dois_tempos = binom.pmf(4, 4, 0.5)

# Probabilidade acumulativa
acumulativa = binom.cdf(4, 4, 0.25)

"""
Concurso com 12 questões, qual a probabilidade de acertar 7 questões
considerando que cada questão tem 4 alternativas?
"""
acertar_prova1 = binom.pmf(7, 12, 0.25)
acertar_prova2 = binom.pmf(7, 12, 0.25) * 100
acertar_prova3 = binom.pmf(12, 12, 0.25) * 100