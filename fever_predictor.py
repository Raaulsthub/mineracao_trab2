import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
import warnings

import tensorflow as tf
from tensorflow import keras


def precision_score(y_true, y_pred):
    correct_preds = 0
    itr = 0
    for i in y_true:
        if y_pred[itr] == i:
            correct_preds += 1
        itr += 1
    return(correct_preds/len(y_true))

RUNALL = 1

warnings.filterwarnings("ignore") # ignoring pandas data[x][y] deprecated warnings

df = pd.read_csv('./data/final.csv')

# PREPARING TRAIN/VALID/TEST 

df.drop(['Unnamed: 0', 'COD_IBGE', 'MUNICIPIO', 'COD_REGIAO_COVID', 'REGIAO_COVID', 'BAIRRO'], axis=1, inplace=True)
df.drop(['PES_PRIV_LIBERDADE', 'BRASILEIRO', 'TESTE_RTPCR', 'TESTE_RAPIDO',
             'TESTE_OUTRO', 'TESTE_CLINICO_EPI', 'TESTE_CLINICO_IMG', 'TESTE_CLINICO', 'RACA_COR_BRANCA',
                 'RACA_COR_NA', 'RACA_COR_PARDA', 'RACA_COR_PRETA', 'RACA_COR_AMARELA', 'RACA_COR_INDIGENA',
                    'FONTE_SUS', 'FONTE_HOSP', 'FONTE_US', 'EVOLUCAO_RECUPERADO', 'EVOLUCAO_OBITO',
                         'EVOLUCAO_OBITO_OC', 'PROFISSIONAL_SAUDE'], axis=1, inplace=True)

print(df.info())

# target = fever?
target = df['FEBRE']
data = df.drop(['FEBRE'], axis=1)

X_train_full, X_test, y_train_full, y_test  = train_test_split(data, target)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full)

if RUNALL:
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(256, activation='relu'))
    model.add(keras.layers.Dense(100, activation='relu'))
    model.add(keras.layers.Dense(2, activation='softmax')) 
        
    model.compile(loss=keras.losses.sparse_categorical_crossentropy,
                    optimizer=keras.optimizers.SGD(), metrics=keras.metrics.sparse_categorical_accuracy)
    history = model.fit(X_train, y_train, epochs=10, validation_data=(X_valid, y_valid))


    model.save('./saved_models/mlp_covid_febre.h5')

# PREDICTOR 2 - LINEAR REGRESSION AND CLASSIFICATION

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