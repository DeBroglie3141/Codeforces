import pandas as pd
import numpy as np

# df_raw : DataFrame sale avec 1000+ lignes, 12 colonnes
# Nettoyez-le pour maximiser le score d'une régression linéaire.
# Affichez le résultat en CSV : print(df_clean.to_csv(index=False))

df = df_raw.copy()

# 1) doublons
df = df.drop_duplicates()

# 2) conversion safe (sauf target)
for col in df.columns:
    if col != "prix":
        df[col] = pd.to_numeric(df[col], errors="coerce")

# 3) garder uniquement numériques
df = df.select_dtypes(include=[np.number])

# 4) supprimer lignes sans target
df = df.dropna(subset=["prix"])

# 5) imputation robuste
df = df.fillna(df.median())

# 6) clipping outliers
for col in df.columns:
    if col != "prix":
        q1 = df[col].quantile(0.01)
        q9 = df[col].quantile(0.99)
        df[col] = df[col].clip(q1, q9)

df_clean = df

print(df_clean.to_csv(index=False))