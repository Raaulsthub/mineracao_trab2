import numpy as np
import pandas as pd

df = pd.read_csv('./data/rules.csv')

print(df.info())

deathdf = df[(df["consequents"] == "frozenset({'EVOLUCAO_OBITO'})") | (df["consequents"] == "frozenset({'EVOLUCAO_OBITO_OC'})")] 

deathdf.to_csv('./data/deathRules.csv')

recoverydf = df[(df["consequents"] == "frozenset({'EVOLUCAO_RECUPERADO'})")] 

recoverydf.to_csv('./data/recoveryRules.csv')

feverdf = df[(df["consequents"] == "frozenset({'FEBRE'})")] 

feverdf.to_csv('./data/feverRules.csv')