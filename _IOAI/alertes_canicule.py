import numpy as np

# 1) température maximale globale
max_temp = np.max(temperatures)

# position (ville, jour) de cette température
ville, jour = np.unravel_index(np.argmax(temperatures), temperatures.shape)

# 2) nombre de relevés > 35°C
nb_releves_35 = np.sum(temperatures > 35)

# 3) nombre de villes avec au moins un jour > 35°C
nb_villes_35 = np.sum(np.any(temperatures > 35, axis=1))

# affichage demandé
print(ville)
print(jour)
print(round(max_temp, 1))
print(nb_releves_35)
print(nb_villes_35)