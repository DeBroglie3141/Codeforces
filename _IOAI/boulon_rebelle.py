import numpy as np

# 1. Quartiles
Q1 = np.percentile(mesures, 25)
Q3 = np.percentile(mesures, 75)

# 2. IQR
IQR = Q3 - Q1

# 3. Bornes
borne_basse = Q1 - 1.5 * IQR
borne_haute = Q3 + 1.5 * IQR

# 4. Détection des outliers
nb_suspects = np.sum((mesures < borne_basse) | (mesures > borne_haute))

# Affichage
print(round(Q1, 2), round(Q3, 2), round(borne_basse, 2), round(borne_haute, 2), nb_suspects)