import pandas as pd
import numpy as np

# df contient 300 produits avec des colonnes textuelles.
# Transformez-le pour que tout soit numérique.
# Affichez : nb colonnes, noms des colonnes, moyenne prix_par_kg

df = df.copy()

# 1) en_stock → 0/1
df["en_stock"] = df["en_stock"].map({"oui": 1, "non": 0})

# 2) prix_par_kg
df["prix_par_kg"] = df["prix"] / df["poids_kg"]

# 3) one-hot encoding catégorie
df = pd.get_dummies(df, columns=["categorie"])

# 4) suppression colonnes textuelles restantes
# (categorie déjà supprimée par get_dummies, mais on sécurise)
df = df.drop(columns=["categorie"], errors="ignore")

# 5) résultats demandés
nb_colonnes = df.shape[1]
colonnes = ",".join(df.columns)
moy_prix_kg = round(df["prix_par_kg"].mean(), 2)

print(nb_colonnes)
print(colonnes)
print(moy_prix_kg)