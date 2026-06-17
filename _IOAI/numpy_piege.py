import numpy as np

ventes = np.array([
    [2500, 3200, 2800, 3100, 2900, 3500, 3800, 4100, 3600, 3300, 2700, 4200],
    [1800, 2100, 1900, 2400, 2200, 2600, 2900, 3100, 2800, 2500, 3200, 2000],
    [3100, 2800, 3300, 2900, 3200, 3600, 3400, 3800, 3500, 3000, 2700, 4000],
    [2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 3500, 3100],
    [1500, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 2700, 2500, 2300, 3200],
])

sauvegarde = ventes.copy()

normalise = ventes - ventes.mean(axis=1, keepdims=True)

mois_top = normalise.argmax(axis=1)

sommes_zero = np.allclose(normalise.sum(axis=1), np.zeros(normalise.shape[0]))

print(f"Originales modifiées: {not np.array_equal(sauvegarde, ventes)}")
print(f"Mois top par magasin: {mois_top}")
print(f"Shape normalisé: {normalise.shape}")
print(f"Vérification somme: {sommes_zero}")