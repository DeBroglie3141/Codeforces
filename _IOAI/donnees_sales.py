import pandas as pd
import numpy as np

# Doublons
df = df.drop_duplicates(subset=['nom', 'ville'])

# Age : convertir les strings en NaN
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Salaire : supprimer les aberrants
df.loc[df['salaire'] < 0, 'salaire'] = np.nan
df.loc[df['salaire'] > 1_000_000, 'salaire'] = np.nan

# Supprimer les lignes trop incomplètes
df = df.dropna(subset=['age', 'salaire'])

print(len(df))
print(df.isna().sum().sum())
print(round(df['salaire'].mean()))
print(int(df['age'].median()))