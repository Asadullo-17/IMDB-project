import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
df=pd.read_csv('imdb_final.csv')

df.rename(columns={'Runtime':'Runtime (minutes)'}, inplace=True)

def convert_votes(v):
    if isinstance(v,int):
        return v    
    v=v.strip().upper()
    if 'M' in v:
        return int(float(v.replace('M',''))*1000000)
    elif 'K' in v:
        return int(float(v.replace('K',''))*1000)
    return int(v)


df['Votes']=df['Votes'].apply(convert_votes)



def convert_box_office(val):
    if pd.isna(val) or not isinstance(val, str) or val.strip()=='':
        return None
    return int(re.sub(r'[^\d]', '', val))

df['Box_office']=df['Box_office'].apply(convert_box_office).astype('Int64')



def convert_runtime(rt):
    hours = minutes = 0
    if not isinstance(rt,str):
        return np.nan
    match=re.search(r'(\d+)\s*hour',rt)
    if match:
        hours=int(match.group(1))
    match=re.search(r'(\d+)\s*minute',rt)
    if match:
        minutes=int(match.group(1))
    return hours*60+minutes

df['Runtime (minutes)']=df['Runtime (minutes)'].apply(convert_runtime)


df['Director']=df['Director'].apply(lambda x: eval(x)[0] if isinstance(x,str) and x.startswith('[') else x)


import ast
df['Genres']=df['Genres'].apply(lambda x: ast.literal_eval(x) if isinstance(x,str) and x.startswith('[') else x)


df['Casts']=df['Casts'].apply(lambda x: ast.literal_eval(x) if isinstance(x,str) and x.startswith('[') else x)
