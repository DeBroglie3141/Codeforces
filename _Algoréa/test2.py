def truc(ind_debut, taille_grp, pos_finales):
    set_grp = set(range(ind_debut, ind_debut + taille_grp))
    
    min_ini = ind_debut
    max_ini = ind_debut + taille_grp - 1
    
    min_final = float('inf')
    max_final = float('-inf')

    for i in range(ind_debut, ind_debut + taille_grp):
        pos = pos_finales[i-1]
        min_final = min(min_final, pos)
        max_final = max(max_final, pos)
    
    for i, pos in enumerate(pos_finales, 1):
        if i not in set_grp:
            if min_final <= pos <= max_final:
                return False
            if i < min_ini and pos > max_final:
                return False
            if i > max_ini and pos < min_final:
                return False
    
    return True

def machin(nb_escar, taille_grp, pos_finales):
    n = 0
    for i in range(1, nb_escar - taille_grp + 2):
        if truc(i, taille_grp, pos_finales):
            n += 1
    return n

nb_escar = int(input())
taille_grp = int(input())
pos_finales = []
for _ in range(nb_escar):
    pos_finales.append(int(input()))

result = machin(nb_escar, taille_grp, pos_finales)
print(result)