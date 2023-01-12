import pandas as pd

data = pd.read_csv('./data/final.csv')
df = pd.read_csv('./data/final.csv')
df.drop(['Unnamed: 0', 'COD_IBGE', 'MUNICIPIO', 'COD_REGIAO_COVID', 'REGIAO_COVID', 'BAIRRO'], axis=1, inplace=True)
df = df.apply(lambda x: x == 1)
df.to_csv('./data/bool.csv')