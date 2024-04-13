import pandas as pd
import numpy as np

df = pd.read_csv('eng.csv', delimiter=",")

q = input("enter a word: ")

x = df.loc[df['word'] == q]
if not x.empty:
    y = x.index[0]
    z = df.loc[y, 'meaning']
    print(z)