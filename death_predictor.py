import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
import warnings

import tensorflow as tf
from tensorflow import keras


# precision calculation function
def precision_score(y_true, y_pred):
    correct_preds = 0
    itr = 0
    for i in y_true:
        if y_pred[itr] == i:
            correct_preds += 1
        itr += 1
    return(correct_preds/len(y_true))

# debugging variable
RUNALL = 1

# ignoring pandas data[x][y] deprecated warnings
warnings.filterwarnings("ignore") #

# reading csv
df = pd.read_csv('./data/final.csv')

# droping unwanted columns 
df.drop(['Unnamed: 0', 'COD_IBGE', 'MUNICIPIO', 'COD_REGIAO_COVID', 'REGIAO_COVID', 'BAIRRO'], axis=1, inplace=True)
df.drop(['PES_PRIV_LIBERDADE', 'BRASILEIRO', 'TESTE_RTPCR', 'TESTE_RAPIDO',
             'TESTE_OUTRO', 'TESTE_CLINICO_EPI', 'TESTE_CLINICO_IMG', 'TESTE_CLINICO', 'RACA_COR_BRANCA',
                 'RACA_COR_NA', 'RACA_COR_PARDA', 'RACA_COR_PRETA', 'RACA_COR_AMARELA', 'RACA_COR_INDIGENA',
                    'FONTE_SUS', 'FONTE_HOSP', 'FONTE_US'], axis=1, inplace=True)


# creating "morreu" column
df['MORREU'] = np.zeros(len(df['EVOLUCAO_RECUPERADO'])).astype(int)
itr = 0
for i in df['EVOLUCAO_RECUPERADO']:
    if i != 1:
        df['MORREU'][itr] = 1
    itr += 1

df.drop(['EVOLUCAO_RECUPERADO', 'EVOLUCAO_OBITO', 'EVOLUCAO_OBITO_OC'], axis=1, inplace=True)

# data and target split
data = df.drop(['MORREU'], axis=1)
target = df['MORREU']

# train, test and valid set split
X_train_full, X_test, y_train_full, y_test  = train_test_split(data, target)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full)


# PREDICTOR 1 - MULTI LAYER PERCEPTRON
if RUNALL:
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(50, activation='relu'))
    model.add(keras.layers.Dense(30, activation='relu'))
    model.add(keras.layers.Dense(2, activation='softmax')) 
        
    model.compile(loss=keras.losses.sparse_categorical_crossentropy,
                    optimizer=keras.optimizers.SGD(), metrics=keras.metrics.sparse_categorical_accuracy)
    history = model.fit(X_train, y_train, epochs=10, validation_data=(X_valid, y_valid))


    model.save('./saved_models/mlp_covid.h5')

# PREDICTOR 2 - LINEAR REGRESSION
if RUNALL:
    model = LinearRegression()
    model.fit(X_train_full, y_train_full)

    linear_model_pred = model.predict(X_test)
    linear_model_pred_bool = np.zeros(len(X_test))
    itr = 0
    for i in linear_model_pred:
        if 1 - i > 0.5:
            linear_model_pred_bool[itr] = 0
        else:
            linear_model_pred_bool[itr] = 1
        itr += 0

    print(precision_score(y_test, linear_model_pred_bool))


# PREDICTOR 3 - RANDOM FOREST
if RUNALL:
    model = RandomForestClassifier()
    model.fit(X_train_full, y_train_full)
    print(precision_score(y_test, model.predict(X_test)))

# PREDICTOR 4 - DUMB PREDICTOR
if RUNALL:
    class DumbPred:
        def __init__(self):
            print("I don't need parameters!")
        def predict(self, a):
            return np.zeros(len(a))

    model = DumbPred()
    print(precision_score(y_test, model.predict(X_test)))