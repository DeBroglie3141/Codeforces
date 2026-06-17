# 4 bugs vicieux. Bonne chance.
# Regle stricte : tu peux uniquement modifier des lignes existantes (pas en ajouter ni en supprimer).

def creer_inventaire(categories):
    return {c: [] for c in categories}

def ajouter_produit(inventaire, categorie, produit):
    inventaire[categorie] += [produit]
    return inventaire

def budget_atteint(prix, cible):
    return abs(sum(prix) - cible) < 1e-9

def creer_callbacks(n):
    return [lambda i=i: i for i in range(n)]