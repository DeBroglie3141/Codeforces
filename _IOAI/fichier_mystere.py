# La variable 'donnees' contient une liste de dictionnaires.
# Chaque dictionnaire est une "ligne" du tableau.

# 1. Combien de lignes ?
nb_lignes = len(donnees)

# 2. Quelles colonnes ? (triées alphabétiquement, séparées par des virgules)
colonnes = sorted(donnees[0].keys())

# 3. Moyenne de la colonne "population" (arrondie à 1 décimale)
moy_population = np.mean([d["population"] for d in donnees])

print(nb_lignes)
print(",".join(colonnes))
print(round(moy_population, 1))