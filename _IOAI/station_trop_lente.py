import numpy as np

# donnees_liste est une liste de 100 listes, chacune contenant 365 températures.
# Exemple : donnees_liste[0][0] = température de la ville 0 au jour 0.

# Approche avec boucles (lente) :
# moyennes = []
# for ville in donnees_liste:
#     total = 0
#     for temp in ville:
#         total += temp
#     moyennes.append(round(total / len(ville), 2))

# Trouvez une approche plus rapide...
truc = np.array(donnees_liste)

moyennes = truc.mean(axis=1)

print(" ".join(f"{m:.2f}" for m in moyennes))