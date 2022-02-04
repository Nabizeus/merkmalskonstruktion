import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_val_score


# Beispiel 2.9 - Online News

# Datensatz

df = pd.read_csv('data/OnlineNewsPopularity.csv', delimiter=',')

df.head()


# Bilde die Logarithmustransformation des Merkmals 'n_tokens_content', das
# die Zahl der Wörter (Tokens) in einer Meldung beschreibt.
#df['log_n_tokens_content'] = np.log10(df['n_tokens_content']+1)
print(df['url'])
#df.head()


