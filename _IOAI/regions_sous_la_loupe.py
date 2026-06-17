# La variable 'donnees' contient la liste de dictionnaires des villes.

# 1. Regroupez les villes par région
#    Indice : un dictionnaire {region: [liste de populations]}
regions = {}

# 2. Pour chaque région, calculez :
#    - nombre de villes
#    - population totale
#    - population moyenne (arrondie à 0 décimales)

for ville in donnees:
    region = ville["region"]
    population = ville["population"]
    
    if region not in regions:
        regions[region] = []
    
    regions[region].append(population)

# 3. Affichez par ordre alphabétique de région :
#    NomRegion nb_villes pop_totale pop_moyenne
for region in sorted(regions.keys()):
    pops = regions[region]
    nb = len(pops)
    total = sum(pops)
    moyenne = round(total / nb)
    print(f"{region} {nb} {total} {moyenne}")

