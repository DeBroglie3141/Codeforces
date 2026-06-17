import numpy as np

orig = releves.copy()
res = releves.copy()

n = len(releves)

for i in range(n):
    if orig[i] == -999.0:
        gauche = orig[i - 1] if orig[i - 1] != -999.0 else None
        droite = orig[i + 1] if orig[i + 1] != -999.0 else None

        if gauche is not None and droite is not None:
            res[i] = (gauche + droite) / 2
        elif gauche is not None:
            res[i] = gauche
        elif droite is not None:
            res[i] = droite

print(" ".join(f"{x:.1f}" for x in res))