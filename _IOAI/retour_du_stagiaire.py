# 4 bugs sur ces fonctions d'analyse de logs.
# Regle stricte : tu peux uniquement modifier des lignes existantes (pas en ajouter ni en supprimer).

def compter_connexions(logs):
    compteur = {}
    for user in logs:
        compteur[user] = compteur.get(user, 0) + 1
    return compteur

def gros_utilisateurs(logs, seuil):
    actifs = set(logs)
    for user in list(actifs):
        if logs.count(user) <= seuil:
            actifs.remove(user)
    return actifs

def trier_descendant(noms):
    return sorted(noms)[::-1]

def utilisateur_le_plus_actif(compteur):
    return max(compteur, key=compteur.get)
