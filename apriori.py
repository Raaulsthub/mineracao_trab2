import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules


# importing data frame
df = pd.read_csv('./data/final.csv')

# **** NEED TO TAKE OUT NON NUMERIC ROWS TO RUN APRIORI ****
df.drop(['Unnamed: 0', 'COD_IBGE', 'MUNICIPIO', 'COD_REGIAO_COVID', 'REGIAO_COVID', 'BAIRRO'], axis=1, inplace=True)

print(df.info())

# Building the model
frq_items = apriori(df, min_support = 0.09, use_colnames = True)

# Collecting the inferred rules in a dataframe
rules = association_rules(frq_items, metric ="lift", min_threshold = 1)
rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])
index = np.arange(len(rules.index))
rules['index'] = index
rules.set_index('index', inplace=True)
rules.to_csv("./data/rules.csv")

# printing rules
print("RULES FOUND: ")
print(rules.head(100)) 