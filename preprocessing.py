import pandas as pd
import numpy as np


MEN = 0
WOMEN = 1

SIM = 1
NAO = 0


# importing the dataframe
data = pd.read_csv('./data/final.csv')

# converting all strings to lowercase
data = data.apply(lambda x: x.astype(str).str.lower())

# filling missing values with zero
data.fillna(0, inplace=True)

# treating inconsistences in rows
# my  line of thought is that, if there is an inconcistence at a row, no value on that row can be trusted
# every time an inconcistence is found, like "SRAG: 12/07/2020", the whole row will be deleted
data = data[(data['GESTANTE'] == 'sim') | (data['GESTANTE'] == 'nao') | (data['GESTANTE'] == 'nan')]
data = data[(data['PROFISSIONAL_SAUDE'] == 'sim') | (data['PROFISSIONAL_SAUDE'] == 'nao') | (data['PROFISSIONAL_SAUDE'] == 'nan')]
data = data[(data['SRAG'] == 'sim') | (data['SRAG'] == 'nao') | (data['SRAG'] == 'nan')]
data = data[(data['PES_PRIV_LIBERDADE'] == 'sim') | (data['PES_PRIV_LIBERDADE'] == 'nao') | (data['PES_PRIV_LIBERDADE'] == 'nan')]

# turning columns into zeros and ones
# note: i want to add .astype(int) in the end
data['SEXO'] = data['SEXO'].map({'masculino': 0, 'feminino': 1}).astype(int)
data['HOSPITALIZADO'] = data['HOSPITALIZADO'].map({'sim': SIM, 'nao': NAO}).astype(int)
data['FEBRE'] = data['FEBRE'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)
data['TOSSE'] = data['TOSSE'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)
data['GARGANTA'] = data['GARGANTA'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)
data['DISPNEIA'] = data['DISPNEIA'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)
data['OUTROS'] = data['OUTROS'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)
data['GESTANTE'] = data['GESTANTE'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)
data['PROFISSIONAL_SAUDE'] = data['PROFISSIONAL_SAUDE'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)
data['SRAG'] = data['SRAG'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)
data['PES_PRIV_LIBERDADE'] = data['PES_PRIV_LIBERDADE'].map({'sim': SIM, 'nao': NAO, 'nan': NAO}).astype(int)

# poping dates out of the data frame
data.drop(['DATA_CONFIRMACAO', 'DATA_SINTOMAS', 'DATA_INCLUSAO', 'DATA_EVOLUCAO', 'DATA_INCLUSAO_OBITO', 'DATA_EVOLUCAO_ESTIMADA'], axis=1, inplace=True)


# list of columns to zero and 1
# - indigena

# list of columns to one hot encoding
# - cod regiao covid, faixa etaria, criterio, evolucao, raca_cor

# dont know
# - fonte de informacao
# - pais nascimento

# one hot encoding

# FAIXA ETARIA
data['IDADE_1'] = np.zeros(len(data['FAIXAETARIA']))
data['IDADE_1_4'] = np.zeros(len(data['FAIXAETARIA']))
data['IDADE_5_9'] = np.zeros(len(data['FAIXAETARIA']))
data['IDADE_10_14'] = np.zeros(len(data['FAIXAETARIA']))
data['IDADE_15_19'] = np.zeros(len(data['FAIXAETARIA']))
data['IDADE_20_29'] = np.zeros(len(data['FAIXAETARIA']))
data['IDADE_30_39'] = np.zeros(len(data['FAIXAETARIA']))
data['IDADE_40_49'] = np.zeros(len(data['FAIXAETARIA']))
data['IDADE_50_59'] = np.zeros(len(data['FAIXAETARIA']))
data['IDADE_60_69'] = np.zeros(len(data['FAIXAETARIA']))
data['IDADE_70_79'] = np.zeros(len(data['FAIXAETARIA']))
data['IDADE_80'] = np.zeros(len(data['FAIXAETARIA']))

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

'''                                             NOTES - all the data bellow is now in lower case
                                                      - all the data bellow was collected on python shell using data['COLUMN_NAME'].unique()

++ COD_IBGE: unique values

++ MUNICIPIO: to many values to track

COD_REGIAO_COVID: [16, 14,  1, 10, 11,  2, 12, 17,  7, 15, 20, 21,  5, 13,  3, 18,  6, 9,  8,  4, 19]

REGIAO_COVID:['BAGE - R22', 'PASSO FUNDO - R17 R18 R19', 'SANTA MARIA - R01 R02',
       'IJUI - R13', 'SANTA ROSA - R14', 'URUGUAIANA - R03',
       'PALMEIRA DAS MISSOES - R15 R20',
       'CAXIAS DO SUL - R23 R24 R25 R26', 'PORTO ALEGRE - R10',
       'PELOTAS - R21', 'LAJEADO - R29 R30', 'GUAIBA - R09',
       'NOVO HAMBURGO - R07', 'ERECHIM - R16', 'CAPAO DA CANOA - R04 R05',
       'CACHOEIRA DO SUL - R27', 'CANOAS - R08', 'CRUZ ALTA - R12',
       'SANTO ANGELO - R11', 'TAQUARA - R06', 'SANTA CRUZ DO SUL - R28']

++ SEXO: ['Feminino', 'Masculino']

++ FAIXA_ETARIA: ['15 a 19', '20 a 29', '40 a 49', '70 a 79', '50 a 59', '80 e mais', '60 a 69', '30 a 39', '10 a 14', '01 a 04', '05 a 09', '<1']

CRITERIO: ['RT-PCR', 'TESTE RÁPIDO', 'Clínico Epidemiológico', 'Clínico-Imagem', 'Clínico', 'Outros testes']

++ DATA_CONFIRMACAO: unique values 
++ DATA_SINTOMAS: unique values
++ DATA_INCLUSAO: unique values
++ DATA_EVOLUCAO: unique values

EVOLUCAO: ['RECUPERADO', 'OBITO', 'OBITO OUTRAS CAUSAS']

++ HOSPITALIZADO: ['NAO', 'SIM']

++ FEBRE: ['NAO', 'SIM', nan]

++ TOSSE: ['NAO', 'SIM', nan]

++ GARGANTA: ['NAO', 'SIM', nan]

++ DISPNEIA: ['NAO', 'SIM', nan]

++ OUTROS: ['NAO', 'SIM', nan]

CONDICOES: [nan, 'Doenças cardíacas crônicas', 'Doença Cardiovascular Crônica',
       'Gestante', 'Diabetes', 'Obesidade',
       'Doenças respiratórias crônicas descompensadas', 'Outros',
       'Imunossupressão',
       'Portador de doenças cromossômicas ou estado de fragilidade imunológica',
       'Diabetes mellitus', 'Outra Pneumatopatia Crônica',
       'Doença Renal Crônica', 'Asma', 'Imunodeficiência',
       'Doenças renais crônicas em estágio avançado (graus 3',
       'Doença Neurológica Crônica', 'Doença Hematológica Crônica',
       'Puérpera (até 45 dias do parto)', 'Doença Hepática Crônica',
       'Pneumatopatia Crônica', 'Puérpera', 'Síndrome de Down',
       'Doença Hematológica Crônic', 'Gestante de alto risco']

++ GESTANTE: ['NAO', 'SIM' + lots of inconsistencies]

++ DATA_INCLUSAO_OBITO: unique values
++ DATA_EVOLUCAO_ESTIMADA: unique values

RACA_COR: ['BRANCA', 'NAO INFORMADO', 'PARDA', 'PRETA', 'AMARELA', 'INDIGENA' + lots of inconsistencies]

INDIGENA: [tribes names + lots of inconsistencies]

++ PROFISSIONAL_SAUDE: ['SIM', 'NAO' + lots of inconsistencies]

BAIRRO: neighborhood names, semi-unique values

++ SRAG: ['SIM', 'NAO' + lots of inconsistencies]

FONTE_INFORMACAO: ['E-SUS', 'SIVEP HOSP' + lots of inconsistencies]

PAIS_NASCIMENTO: [countries names + lots of inconsistencies]

++ PES_PRIV_LIBERDADE: ['SIM', 'NAO' + lots of inconsistencies]
'''