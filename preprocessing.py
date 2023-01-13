import pandas as pd
import numpy as np
import warnings

# ignoring pandas data[x][y] deprecated warnings
warnings.filterwarnings("ignore") 

# defines
MEN = 0
WOMEN = 1

SIM = 1
NAO = 0

BRASILEIRO = 1
ESTRANGEIRO = 0

# importing the dataframe
data = pd.read_csv('./data/saudeRS_2022.csv', sep=';')

# printing initial data frame struct
print('Initial Data Frame structure: ')
print(data.info())

# converting all strings to lowercase
data = data.apply(lambda x: x.astype(str).str.lower())

# filling missing values with zero
data.fillna(0, inplace=True)

# turning columns into zeros and ones
data['SEXO'] = data['SEXO'].map({'masculino': 0, 'feminino': 1}).astype(int)
data['HOSPITALIZADO'] = data['HOSPITALIZADO'].map({'sim': SIM, 'nao': NAO}).astype(int)
data['FEBRE'] = data['FEBRE'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)
data['TOSSE'] = data['TOSSE'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)
data['GARGANTA'] = data['GARGANTA'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)
data['DISPNEIA'] = data['DISPNEIA'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)
data['OUTROS'] = data['OUTROS'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)
data['GESTANTE'] = data['GESTANTE'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)
data['PROFISSIONAL_SAUDE'] = data['PROFISSIONAL_SAUDE'].map({'sim': SIM, 'nao': NAO, 'nao informado': NAO}).astype(int)
data['SRAG'] = data['SRAG'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)
data['PES_PRIV_LIBERDADE'] = data['PES_PRIV_LIBERDADE'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)

# condicoes will be implemented as yes or no
aux  = np.zeros(len(data['CONDICOES'])).astype(int)
itr = 0
for i in data['CONDICOES']:
       if i != 'nan':
              aux[itr] = SIM
       itr += 1

data['CONDICOES'] = aux

# pais_nascimento will be implemented as yes or no
data['BRASILEIRO'] = np.ones(len(data['PAIS_NASCIMENTO'])).astype(int)
itr = 0
for i in data['PAIS_NASCIMENTO']:
       if i != 'brasil':
              data['BRASILEIRO'][itr] = ESTRANGEIRO
       itr += 1
       
data.drop(['PAIS_NASCIMENTO'], axis=1, inplace=True)

# etnia indigena will be implemented as yes or no
aux  = np.zeros(len(data['ETNIA_INDIGENA'])).astype(int)
itr = 0
for i in data['ETNIA_INDIGENA']:
       if i != 'nan' and i != 'nao encontrado':
              aux[itr] = SIM
       itr += 1
data['ETNIA_INDIGENA'] = aux

# poping dates out of the data frame/
data.drop(['DATA_CONFIRMACAO', 'DATA_SINTOMAS', 'DATA_INCLUSAO', 'DATA_EVOLUCAO', 'DATA_INCLUSAO_OBITO', 'DATA_EVOLUCAO_ESTIMADA'], axis=1, inplace=True)

# one hot encoding

# FAIXA ETARIA
data['IDADE_1'] = np.zeros(len(data['FAIXAETARIA'])).astype(int)
data['IDADE_1_4'] = np.zeros(len(data['FAIXAETARIA'])).astype(int)
data['IDADE_5_9'] = np.zeros(len(data['FAIXAETARIA'])).astype(int)
data['IDADE_10_14'] = np.zeros(len(data['FAIXAETARIA'])).astype(int)
data['IDADE_15_19'] = np.zeros(len(data['FAIXAETARIA'])).astype(int)
data['IDADE_20_29'] = np.zeros(len(data['FAIXAETARIA'])).astype(int)
data['IDADE_30_39'] = np.zeros(len(data['FAIXAETARIA'])).astype(int)
data['IDADE_40_49'] = np.zeros(len(data['FAIXAETARIA'])).astype(int)
data['IDADE_50_59'] = np.zeros(len(data['FAIXAETARIA'])).astype(int)
data['IDADE_60_69'] = np.zeros(len(data['FAIXAETARIA'])).astype(int)
data['IDADE_70_79'] = np.zeros(len(data['FAIXAETARIA'])).astype(int)
data['IDADE_80'] = np.zeros(len(data['FAIXAETARIA'])).astype(int)

itr = 0
for i in data['FAIXAETARIA']:
       if i == '<1':
              data['IDADE_1'][itr] = 1
       elif i == '01 a 04':
              data['IDADE_1_4'][itr] = 1
       elif i == '05 a 09':
              data['IDADE_5_9'][itr] = 1
       elif i == '10 a 14':
              data['IDADE_10_14'][itr] = 1
       elif i == '15 a 19':
              data['IDADE_15_19'][itr] = 1
       elif i == '20 a 29':
              data['IDADE_20_29'][itr] = 1
       elif i == '30 a 39':
              data['IDADE_30_39'][itr] = 1
       elif i == '40 a 49':
              data['IDADE_40_49'][itr] = 1
       elif i == '50 a 59':
              data['IDADE_50_59'][itr] = 1
       elif i == '60 a 69':
              data['IDADE_60_69'][itr] = 1
       elif i == '70 a 79':
              data['IDADE_70_79'][itr] = 1
       elif i == '80 e mais':
              data['IDADE_80'][itr] = 1
       itr += 1


data.drop(['FAIXAETARIA'], axis=1, inplace=True)

# CRITERIO
data['TESTE_RTPCR'] = np.zeros(len(data['CRITERIO'])).astype(int)
data['TESTE_RAPIDO'] = np.zeros(len(data['CRITERIO'])).astype(int)
data['TESTE_OUTRO'] = np.zeros(len(data['CRITERIO'])).astype(int)
data['TESTE_CLINICO_EPI'] = np.zeros(len(data['CRITERIO'])).astype(int)
data['TESTE_CLINICO_IMG'] = np.zeros(len(data['CRITERIO'])).astype(int)
data['TESTE_CLINICO'] = np.zeros(len(data['CRITERIO'])).astype(int)

itr = 0
for i in data['CRITERIO']:
       if i == 'rt-pcr':
              data['TESTE_RTPCR'][itr] = 1
       elif i == 'teste rápido':
              data['TESTE_RAPIDO'][itr] = 1
       elif i == 'outros testes':
              data['TESTE_OUTRO'][itr] = 1
       elif i == 'clínico epidemiológico':
              data['TESTE_CLINICO_EPI'][itr] = 1
       elif i == 'clínico-imagem':
              data['TESTE_CLINICO_IMG'][itr] = 1
       elif i == 'clínico':
              data['TESTE_CLINICO'][itr] = 1
       itr += 1

data.drop(['CRITERIO'], axis=1, inplace=True)

# EVOLUCAO ['RECUPERADO', 'OBITO', 'OBITO OUTRAS CAUSAS']
data['EVOLUCAO_RECUPERADO'] = np.zeros(len(data['EVOLUCAO'])).astype(int)
data['EVOLUCAO_OBITO'] = np.zeros(len(data['EVOLUCAO'])).astype(int)
data['EVOLUCAO_OBITO_OC'] = np.zeros(len(data['EVOLUCAO'])).astype(int)

itr = 0
for i in data['EVOLUCAO']:
       if i == 'recuperado':
              data['EVOLUCAO_RECUPERADO'][itr] = 1
       elif i == 'obito':
              data['EVOLUCAO_OBITO'][itr] = 1
       elif i == 'obito outras causas':
              data['EVOLUCAO_OBITO_OC'][itr] = 1
       itr += 1

data.drop(['EVOLUCAO'], axis=1, inplace=True)


# RACA_COR 'BRANCA', 'NAO INFORMADO', 'PARDA', 'PRETA', 'AMARELA', 'INDIGENA'
data['RACA_COR_BRANCA'] = np.zeros(len(data['RACA_COR'])).astype(int)
data['RACA_COR_NA'] = np.zeros(len(data['RACA_COR'])).astype(int)
data['RACA_COR_PARDA'] = np.zeros(len(data['RACA_COR'])).astype(int)
data['RACA_COR_PRETA'] = np.zeros(len(data['RACA_COR'])).astype(int)
data['RACA_COR_AMARELA'] = np.zeros(len(data['RACA_COR'])).astype(int)
data['RACA_COR_INDIGENA'] = np.zeros(len(data['RACA_COR'])).astype(int)

itr = 0
for i in data['RACA_COR']:
       if i == 'branca':
              data['RACA_COR_BRANCA'][itr] = 1
       elif i == 'nao informado':
              data['RACA_COR_NA'][itr] = 1
       elif i == 'parda':
              data['RACA_COR_PARDA'][itr] = 1
       elif i == 'preta':
              data['RACA_COR_PRETA'][itr] = 1
       elif i == 'amarela':
              data['RACA_COR_AMARELA'][itr] = 1
       elif i == 'indigena':
              data['RACA_COR_INDIGENA'][itr] = 1
       itr += 1

data.drop(['RACA_COR'], axis=1, inplace=True)

# FONTE DE INFORMACAO:  ['E-SUS', 'SIVEP HOSP', 'SIVEP US', nan]
data['FONTE_SUS'] = np.zeros(len(data['FONTE_INFORMACAO'])).astype(int)
data['FONTE_HOSP'] = np.zeros(len(data['FONTE_INFORMACAO'])).astype(int)
data['FONTE_US'] = np.zeros(len(data['FONTE_INFORMACAO'])).astype(int)

itr = 0
for i in data['FONTE_INFORMACAO']:
       if i == 'e-sus':
              data['FONTE_SUS'][itr] = 1
       elif i == 'sivep hosp':
              data['FONTE_HOSP'][itr] = 1
       elif i == 'sivep us':
              data['FONTE_US'][itr] = 1
       itr += 1 

data.drop(['FONTE_INFORMACAO'], axis=1, inplace=True)


# printing final structure
print('Final Data Frame structure: ')
print(data.info())

# saving data
data.to_csv('./data/final.csv')


'''                                             NOTES - all the data bellow is now in lower case
                                                      - all the data bellow was collected on python shell using data['COLUMN_NAME'].unique()

++ COD_IBGE: unique values

++ MUNICIPIO: to many values to track

++ COD_REGIAO_COVID: [16, 14,  1, 10, 11,  2, 12, 17,  7, 15, 20, 21,  5, 13,  3, 18,  6, 9,  8,  4, 19]

++ REGIAO_COVID:['BAGE - R22', 'PASSO FUNDO - R17 R18 R19', 'SANTA MARIA - R01 R02',
       'IJUI - R13', 'SANTA ROSA - R14', 'URUGUAIANA - R03',
       'PALMEIRA DAS MISSOES - R15 R20',
       'CAXIAS DO SUL - R23 R24 R25 R26', 'PORTO ALEGRE - R10',
       'PELOTAS - R21', 'LAJEADO - R29 R30', 'GUAIBA - R09',
       'NOVO HAMBURGO - R07', 'ERECHIM - R16', 'CAPAO DA CANOA - R04 R05',
       'CACHOEIRA DO SUL - R27', 'CANOAS - R08', 'CRUZ ALTA - R12',
       'SANTO ANGELO - R11', 'TAQUARA - R06', 'SANTA CRUZ DO SUL - R28']

++ SEXO: ['Feminino', 'Masculino']

++ FAIXA_ETARIA: ['15 a 19', '20 a 29', '40 a 49', '70 a 79', '50 a 59', '80 e mais', '60 a 69', '30 a 39', '10 a 14', '01 a 04', '05 a 09', '<1']

++ CRITERIO: [RT-PCR', 'TESTE RÁPIDO', 'Outros Testes', 'Clínico Epidemiológico', 'Clínico-Imagem', 'Clínico', 'Outros testes']
++ DATA_CONFIRMACAO: unique values 
++ DATA_SINTOMAS: unique values
++ DATA_INCLUSAO: unique values
++ DATA_EVOLUCAO: unique values

++ EVOLUCAO: ['RECUPERADO', 'OBITO', 'OBITO OUTRAS CAUSAS']

++ HOSPITALIZADO: ['NAO', 'SIM']

++ FEBRE: ['NAO', 'SIM', nan]

++ TOSSE: ['NAO', 'SIM', nan]

++ GARGANTA: ['NAO', 'SIM', nan]

++ DISPNEIA: ['NAO', 'SIM', nan]

++ OUTROS: ['NAO', 'SIM', nan]

++ CONDICOES: ['nan', 'unique combinations']

++ GESTANTE: ['NAO', 'SIM']

++ DATA_INCLUSAO_OBITO: unique values
++ DATA_EVOLUCAO_ESTIMADA: unique values

++ RACA_COR: ['BRANCA', 'NAO INFORMADO', 'PARDA', 'PRETA', 'AMARELA', 'INDIGENA']

++ INDIGENA: [tribes names, 'nan', 'nao encontrado']

++ PROFISSIONAL_SAUDE: ['NAO', 'NAO INFORMADO', 'SIM'

++ BAIRRO: neighborhood names, semi-unique values

++ SRAG: ['NAO', 'SIM']

++ FONTE_INFORMACAO: ['E-SUS', 'SIVEP HOSP', 'SIVEP US', nan]

++ PAIS_NASCIMENTO: [countries names]

++ PES_PRIV_LIBERDADE: ['SIM', 'NAO']
'''