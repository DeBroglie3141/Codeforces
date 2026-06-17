# La variable 'donnees' contient la liste de dictionnaires des villes.

# 1. Trouvez les villes avec population > 400 000
#    Triez-les par population décroissante
#    Affichez leurs noms séparés par des virgules
grandes_villes = [d for d in donnees if d["population"] > 400000]
grandes_villes_sorted = sorted(grandes_villes, key=lambda x: x["population"], reverse=True)
noms = [d["ville"] for d in grandes_villes_sorted]
print(",".join(noms))

# 2. Parmi ces grandes villes, calculez la densité (population/superficie)
#    Trouvez celle avec la plus haute densité
densites = [(d["ville"], d["population"] / d["superficie"]) for d in grandes_villes_sorted]
ville_dense, densite_max = max(densites, key=lambda x: x[1])

print(ville_dense, round(densite_max))