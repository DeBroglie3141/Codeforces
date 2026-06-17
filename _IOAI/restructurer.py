import pandas as pd
import numpy as np

# ventes : DataFrame avec colonnes magasin, mois, montant
# Créez un tableau croisé et répondez aux questions.
# 1) tableau croisé (somme des ventes)
pivot = ventes.pivot_table(
    index="magasin",
    columns="mois",
    values="montant",
    aggfunc="sum",
    fill_value=0
)

# garantir ordre des mois (0-11 ou 1-12 selon dataset)
pivot = pivot.reindex(sorted(pivot.columns), axis=1)

# affichage ligne par ligne
for _, row in pivot.iterrows():
    print(" ".join(map(str, row.values)))

# 2) magasin avec meilleur CA annuel
ca_par_magasin = pivot.sum(axis=1)
best_magasin = ca_par_magasin.idxmax()

# 3) mois le plus rentable tous magasins confondus
ca_par_mois = pivot.sum(axis=0)
best_mois = ca_par_mois.idxmax()

print(best_magasin)
print(best_mois)