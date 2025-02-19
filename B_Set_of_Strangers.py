N = int(input())

for _ in range(N):
    n, m = map(int, input().split())
    grille = [list(map(int, input().split())) for _ in range(n)]
    nbr_modifs_par_groupe = {}

    for i in range(n):
        for j in range(m):
            if grille[i][j] != '.':
                for k,l in ((i-1, j), (i, j-1), (i, j+1), (i+1, j)):
                    if (0 <= k <= n-1) and (0 <= l <= m-1) and (grille[i][j] == grille[k][l]):
                        if grille[i][j] in nbr_modifs_par_groupe:
                            nbr_modifs_par_groupe[grille[i][j]] += 1
                        else:
                            nbr_modifs_par_groupe[grille[i][j]] = 1
                        grille[i][j] = '.'
    
    groupes = set()
    for ligne in grille:
        groupes.update(ligne)

    for groupe in groupes:
        if groupe in nbr_modifs_par_groupe:
            nbr_modifs_par_groupe[groupe] += 1
        else:
            nbr_modifs_par_groupe[groupe] = 1

    nbr_modifs_par_groupe['.'] = 0

    liste_nbr_modifs = nbr_modifs_par_groupe.values()
    nbr_modifs = sum(liste_nbr_modifs) - max(liste_nbr_modifs)

    print(nbr_modifs)
