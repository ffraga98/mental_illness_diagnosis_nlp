# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 12:39:06 2023

@author: Lu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df=pd.read_csv('./mental_disorders_reddit.csv')


# Cantidad de campos nulos en cada columna 
#print(df.isnull().sum())

df=df.dropna(how='any')
#%% Chequeo de correcta importacion de los datos de la DB
#print(df['selftext'][0].find('[removed]'))
#print(df['selftext'].str.contains('\[removed\]'))
#%%

df=df[df['selftext'].str.contains('\[removed\]')==False]
print(df.head()) 
# Chequeo de la correcta eliminacion de los campos null
#print(df.shape)
#print(df.isnull().sum())

#%%
print(df)

#%% Procesamiento de Data
table = df['subreddit'].value_counts()

labels = table.axes[0].array
sizes = table.array

# Chequeo de creacion de arrays
#print(labels)
#print(sizes)

custom_colours = ['b', 'g','r','c','m','y']

plt.figure(figsize=(20, 6), dpi=227)
plt.subplot(1, 2, 1)
plt.pie(sizes, labels = labels, textprops={'fontsize': 10}, startangle=140, 
       autopct='%1.0f%%', colors=custom_colours, explode=[0,0,0,0,0.05,0])

plt.subplot(1, 2, 2)
sns.barplot(x = labels, y = sizes, palette= 'viridis')

plt.show()

#%% Cantidad de palabras y caracteres
df['title_total'] = df['title'].apply(lambda x: len(x.split()))

def count_total_words(text):
    char = 0
    for word in text.split():
        char += len(word)
    return char

df['title_chars'] = df["title"].apply(count_total_words)

df['text_total'] = df['selftext'].apply(lambda x: len(x.split()))

def count_total_words(text):
    char = 0
    for word in text.split():
        char += len(word)
    return char

df['text_chars'] = df["selftext"].apply(count_total_words)

#%% Graficos correspondientes a los datos obtenidos

plt.figure(figsize = (10, 6))
sns.kdeplot(x = df['title_total'], hue= df['subreddit'], palette= 'husl')
plt.title('Number of word of title by subreddit')
plt.xlim((0,40))
plt.show()

plt.figure(figsize = (10, 6))
sns.kdeplot(x = df['title_chars'], hue= df['subreddit'], palette= 'husl')
plt.title('Number of char of title by subreddit')
plt.xlim((0,150))
plt.show()

#%%
plt.figure(figsize = (10, 6))
sns.kdeplot(x = df['text_total'], hue= df['subreddit'], palette= 'husl')
plt.title('Number of word of selftext by subreddit')
plt.xlim((-1,1000))
plt.show()

plt.figure(figsize = (10, 6))
sns.kdeplot(x = df['text_chars'], hue= df['subreddit'], palette= 'husl')
plt.title('Number of char of selftext by subreddit')
plt.xlim((-1,5000))
plt.show()

#%% 
print(df['title_total'])

#%%
def mental_disorders(ex):
    if ex=='BPD':
        return 'BPD'
    elif ex=='Anxiety':
        return 'Anxiety'
    elif ex=='depression':
        return 'depression'
    else:
        return 'others'
    
#%%
df['subreddit']=df['subreddit'].apply(mental_disorders)
print(df)

#%%
df=df[df['subreddit'].str.contains('others')==False]
print(df)