import numpy as np
import pandas as pd

df = pd.read_csv('./data/final.csv')

# **** NEED TO TAKE OUT NON NUMERIC AND UNINTERESTING ROWS TO RUN APRIORI ****
df.drop(['Unnamed: 0', 'COD_IBGE', 'MUNICIPIO', 'COD_REGIAO_COVID', 'REGIAO_COVID', 'BAIRRO',
        'TESTE_RTPCR', 'TESTE_RAPIDO', 'TESTE_OUTRO', 'TESTE_CLINICO_EPI', 'TESTE_CLINICO_IMG',
        'TESTE_CLINICO', 'PES_PRIV_LIBERDADE', 'BRASILEIRO', 'RACA_COR_BRANCA', 'RACA_COR_NA',
        'RACA_COR_PARDA', 'RACA_COR_PRETA', 'RACA_COR_AMARELA', 'RACA_COR_INDIGENA', 'FONTE_SUS',
        'FONTE_HOSP', 'FONTE_US'], axis=1, inplace=True)

df = df.astype(bool)

print(df.info())

# saving data
df.to_csv('./data/simpleDF.csv')