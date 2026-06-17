# donnees : liste de dicts des villes (avec 'region')
# donnees_eco : liste de dicts économiques par région (avec 'region', 'pib_par_hab')

# 1. Créez un moyen rapide de retrouver les données éco d'une région
eco_par_region = {
    d["region"]: d for d in donnees_eco
}

# 2. Pour chaque ville, calculez le score = population * pib_par_hab / 1_000_000_000
resultats = []

for ville in donnees:
    region = ville["region"]
    population = ville["population"]
    
    pib_par_hab = eco_par_region[region]["pib_par_hab"]
    
    score = population * pib_par_hab / 1_000_000_000
    
    resultats.append({
        "ville": ville["ville"],
        "score": score
    })


# 3. Triez par score décroissant et affichez
resultats.sort(key=lambda x: x["score"], reverse=True)

for r in resultats:
    print(f"{r['ville']} {round(r['score'], 1)}")