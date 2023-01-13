import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

df = pd.read_csv("data/simpleDF.csv")

data = df

print(df.info())

# vetor de faixas etárias
x = np.arange(12)

# filtrando apenas pessoas que morreram para o data frame
df = df[(df['EVOLUCAO_OBITO'] == True) | (df['EVOLUCAO_OBITO_OC'] == True)]

# vetor de mortes por faixa etaria absoluto
yAbs = [df['IDADE_1'].value_counts()[True], df['IDADE_1_4'].value_counts()[True], df['IDADE_5_9'].value_counts()[True],
    df['IDADE_10_14'].value_counts()[True], df['IDADE_15_19'].value_counts()[True], df['IDADE_20_29'].value_counts()[True],
    df['IDADE_30_39'].value_counts()[True], df['IDADE_40_49'].value_counts()[True], df['IDADE_50_59'].value_counts()[True],
    df['IDADE_60_69'].value_counts()[True], df['IDADE_70_79'].value_counts()[True], df['IDADE_80'].value_counts()[True]]

# vetor de mortes em porcentagem
y = []

for i in yAbs:
    y.append((i * 100) / len(df))

# plot idade - % mortalidade absoluta

new_list = range(math.floor(min(x)), math.ceil(max(x))+1)
plt.xticks(new_list)

plt.xlabel("Faixa Etária ")
plt.ylabel("Porcentagem de Mortes")

plt.title("Porcentagem total de mortes por faixa etária")

plt.plot(x, y, linewidth=3, color="red")

plt.show()

# Preparando o plot de mortalidade por porcentagem total da faixa etária

df = data

# criando vetor de mortes / total da faixa etária
y = []

y = [(len(df[((df['EVOLUCAO_OBITO'] == True) | (df['EVOLUCAO_OBITO_OC'] == True)) & (df['IDADE_1'] == True)]) * 100)
    / len(df[df['IDADE_1'] == True]),
    (len(df[((df['EVOLUCAO_OBITO'] == True) | (df['EVOLUCAO_OBITO_OC'] == True)) & (df['IDADE_1_4'] == True)]) * 100)
    / len(df[df['IDADE_1_4'] == True]),
    (len(df[((df['EVOLUCAO_OBITO'] == True) | (df['EVOLUCAO_OBITO_OC'] == True)) & (df['IDADE_5_9'] == True)]) * 100)
    / len(df[df['IDADE_5_9'] == True]),
    (len(df[((df['EVOLUCAO_OBITO'] == True) | (df['EVOLUCAO_OBITO_OC'] == True)) & (df['IDADE_10_14'] == True)]) * 100)
    / len(df[df['IDADE_10_14'] == True]),
    (len(df[((df['EVOLUCAO_OBITO'] == True) | (df['EVOLUCAO_OBITO_OC'] == True)) & (df['IDADE_15_19'] == True)]) * 100)
    / len(df[df['IDADE_15_19'] == True]),
    (len(df[((df['EVOLUCAO_OBITO'] == True) | (df['EVOLUCAO_OBITO_OC'] == True)) & (df['IDADE_20_29'] == True)]) * 100)
    / len(df[df['IDADE_20_29'] == True]),
    (len(df[((df['EVOLUCAO_OBITO'] == True) | (df['EVOLUCAO_OBITO_OC'] == True)) & (df['IDADE_30_39'] == True)]) * 100)
    / len(df[df['IDADE_30_39'] == True]),
    (len(df[((df['EVOLUCAO_OBITO'] == True) | (df['EVOLUCAO_OBITO_OC'] == True)) & (df['IDADE_40_49'] == True)]) * 100)
    / len(df[df['IDADE_40_49'] == True]),
    (len(df[((df['EVOLUCAO_OBITO'] == True) | (df['EVOLUCAO_OBITO_OC'] == True)) & (df['IDADE_50_59'] == True)]) * 100)
    / len(df[df['IDADE_50_59'] == True]),
    (len(df[((df['EVOLUCAO_OBITO'] == True) | (df['EVOLUCAO_OBITO_OC'] == True)) & (df['IDADE_60_69'] == True)]) * 100)
    / len(df[df['IDADE_60_69'] == True]),
    (len(df[((df['EVOLUCAO_OBITO'] == True) | (df['EVOLUCAO_OBITO_OC'] == True)) & (df['IDADE_70_79'] == True)]) * 100)
    / len(df[df['IDADE_70_79'] == True]),
    (len(df[((df['EVOLUCAO_OBITO'] == True) | (df['EVOLUCAO_OBITO_OC'] == True)) & (df['IDADE_80'] == True)]) * 100)
    / len(df[df['IDADE_80'] == True])]

# plot idade - % mortalidade / faixa etaria

new_list = range(math.floor(min(x)), math.ceil(max(x))+1)
plt.xticks(new_list)

plt.xlabel("Faixa Etária ")
plt.ylabel("Porcentagem de Mortes por faixa etária ")

plt.title("Porcentagem de mortes pelo total da faixa etária")

plt.plot(x, y, linewidth=3, color="blue")

plt.show()

# Preparando para plotar um grafico de febre por % total do data frame

# filtrando apenas pessoas com febre para o data frame
df = df[df['FEBRE'] == True]

# vetor de febre por faixa etaria absoluto
yAbs = [df['IDADE_1'].value_counts()[True], df['IDADE_1_4'].value_counts()[True], df['IDADE_5_9'].value_counts()[True],
    df['IDADE_10_14'].value_counts()[True], df['IDADE_15_19'].value_counts()[True], df['IDADE_20_29'].value_counts()[True],
    df['IDADE_30_39'].value_counts()[True], df['IDADE_40_49'].value_counts()[True], df['IDADE_50_59'].value_counts()[True],
    df['IDADE_60_69'].value_counts()[True], df['IDADE_70_79'].value_counts()[True], df['IDADE_80'].value_counts()[True]]

# vetor de mortes em porcentagem
y = []

for i in yAbs:
    y.append((i * 100) / len(df))

# plot idade - % mortalidade absoluta

new_list = range(math.floor(min(x)), math.ceil(max(x))+1)
plt.xticks(new_list)

plt.xlabel("Faixa Etária ")
plt.ylabel("Porcentagem de Febre")

plt.title("Porcentagem total de Febre por faixa etária")

plt.plot(x, y, linewidth=3, color="purple")

plt.show()

# Preparando o plot de mortalidade por porcentagem total da faixa etária

df = data

# criando vetor de mortes / total da faixa etária
y = []

y = [(len(df[(df['FEBRE'] == True) & (df['IDADE_1'] == True)]) * 100)
    / len(df[df['IDADE_1'] == True]),
    (len(df[(df['FEBRE'] == True) & (df['IDADE_1_4'] == True)]) * 100)
    / len(df[df['IDADE_1_4'] == True]),
    (len(df[(df['FEBRE'] == True) & (df['IDADE_5_9'] == True)]) * 100)
    / len(df[df['IDADE_5_9'] == True]),
    (len(df[(df['FEBRE'] == True) & (df['IDADE_10_14'] == True)]) * 100)
    / len(df[df['IDADE_10_14'] == True]),
    (len(df[(df['FEBRE'] == True) & (df['IDADE_15_19'] == True)]) * 100)
    / len(df[df['IDADE_15_19'] == True]),
    (len(df[(df['FEBRE'] == True) & (df['IDADE_20_29'] == True)]) * 100)
    / len(df[df['IDADE_20_29'] == True]),
    (len(df[(df['FEBRE'] == True) & (df['IDADE_30_39'] == True)]) * 100)
    / len(df[df['IDADE_30_39'] == True]),
    (len(df[(df['FEBRE'] == True) & (df['IDADE_40_49'] == True)]) * 100)
    / len(df[df['IDADE_40_49'] == True]),
    (len(df[(df['FEBRE'] == True) & (df['IDADE_50_59'] == True)]) * 100)
    / len(df[df['IDADE_50_59'] == True]),
    (len(df[(df['FEBRE'] == True) & (df['IDADE_60_69'] == True)]) * 100)
    / len(df[df['IDADE_60_69'] == True]),
    (len(df[(df['FEBRE'] == True) & (df['IDADE_70_79'] == True)]) * 100)
    / len(df[df['IDADE_70_79'] == True]),
    (len(df[(df['FEBRE'] == True) & (df['IDADE_80'] == True)]) * 100)
    / len(df[df['IDADE_80'] == True])]

# plot idade - % mortalidade / faixa etaria

new_list = range(math.floor(min(x)), math.ceil(max(x))+1)
plt.xticks(new_list)

plt.xlabel("Faixa Etária ")
plt.ylabel("Porcentagem de Febre por faixa etária ")

plt.title("Porcentagem de Febre pelo total da Faixa Etária")

plt.plot(x, y, linewidth=3, color="green")

plt.show()