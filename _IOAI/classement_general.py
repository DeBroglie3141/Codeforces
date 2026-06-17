import numpy as np

mask = ~np.isnan(notes)

notes_clean = np.nan_to_num(notes, nan=0.0)

weighted_sum = np.sum(notes_clean * coeffs, axis=1)

coeff_sum = np.sum(mask * coeffs, axis=1)

moyennes = weighted_sum / coeff_sum

rangs = np.argsort(np.argsort(-moyennes)) + 1

for m, r in zip(moyennes, rangs):
    print(f"{m:.2f} {r}")