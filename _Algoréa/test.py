def truc(n, pos_finales):
    pos_finales = [x - 1 for x in pos_finales] 
    grp_max = 1
    diff_ini = [0] * n
    diff_fin = [0] * n
    
    for machin in range(n - 1):
        pr_escar = pos_finales[machin]
        taille_diff = 0
        
        for j in range(machin + 1, n):
            act_escar = pos_finales[j]
            
            diff_ini[taille_diff] = j - machin
            diff_fin[taille_diff] = act_escar - pr_escar
            
            if diff_fin[taille_diff] > 0:
                taille_diff += 1
        
        if taille_diff > 0:
            grp_act = 1
            
            for i in range(taille_diff):
                if diff_ini[i] == diff_fin[i]:
                    grp_act += 1
            
            if grp_act > grp_max:
                grp_max = grp_act
                if grp_max == n:
                    return grp_max
    
    return grp_max

n = int(input())
pos_finales = [int(input()) for _ in range(n)]

print(truc(n, pos_finales))