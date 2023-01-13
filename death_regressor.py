import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import warnings

# ignoring pandas data[x][y] deprecated warnings
warnings.filterwarnings("ignore")

# importing data
df = pd.read_csv('./data/final.csv')

# preaparing data
df.drop(['Unnamed: 0', 'COD_IBGE', 'MUNICIPIO', 'COD_REGIAO_COVID', 'REGIAO_COVID', 'BAIRRO'], axis=1, inplace=True)
df.drop(['PES_PRIV_LIBERDADE', 'BRASILEIRO', 'TESTE_RTPCR', 'TESTE_RAPIDO',
             'TESTE_OUTRO', 'TESTE_CLINICO_EPI', 'TESTE_CLINICO_IMG', 'TESTE_CLINICO', 'RACA_COR_BRANCA',
                 'RACA_COR_NA', 'RACA_COR_PARDA', 'RACA_COR_PRETA', 'RACA_COR_AMARELA', 'RACA_COR_INDIGENA',
                    'FONTE_SUS', 'FONTE_HOSP', 'FONTE_US'], axis=1, inplace=True)

df['MORREU'] = np.zeros(len(df['EVOLUCAO_RECUPERADO'])).astype(int)
itr = 0
for i in df['EVOLUCAO_RECUPERADO']:
    if i != 1:
        df['MORREU'][itr] = 1
    itr += 1
df.drop(['EVOLUCAO_RECUPERADO', 'EVOLUCAO_OBITO', 'EVOLUCAO_OBITO_OC'], axis=1, inplace=True)

# preparing sets
data = df.drop(['MORREU'], axis=1)
target = df['MORREU']
X_train_full, X_test, y_train_full, y_test  = train_test_split(data, target)


# the following linear regressor was used to output float results - the biggest output will
# be the higher death probability
model = LinearRegression()
model.fit(X_train_full, y_train_full)

print("GENERAL PREDICTIONS: ")
print(model.predict(X_test))
print(f'The avarege prediction on general cases is {np.average(model.predict(X_test))}')
print()

df = df[df['MORREU'] == 1]
data = df.drop(['MORREU'], axis=1)
print("PREDICTIONS FOR DEATH CASES")
print(model.predict(data))
print(f'The avarege prediction on the cases where death happened is {np.average(model.predict(data))}')
print()