# 4 bugs sur ces fonctions de gestion de notes.
# Regle stricte : tu peux uniquement modifier des lignes existantes (pas en ajouter ni en supprimer).

def creer_grille(n_eleves, n_matieres):
    return [[0 for _ in range(n_matieres)] for _ in range(n_eleves)]

def moyennes_eleves(notes):
    n_eleves = len(notes)
    n_matieres = len(notes[0])
    moyennes = [0.0] * n_eleves
    for eleve in range(n_eleves):
        total = 0
        for matiere in range(n_matieres):
            total += notes[eleve][matiere]
        moyennes[eleve] = total / n_matieres
    return moyennes