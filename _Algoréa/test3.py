def truc(n, pos_finales):
    pos_finale = [0] * n
    for i in range(n):
        pos_finale[pos_finales[i] - 1] = i
    
    min_taille = n
    for start in range(n):
        if min_taille <= 1:
            break
            
        positions = set()
        escargots = set()
        
        pos = start
        while pos not in positions:
            positions.add(pos)
            escargot = pos + 1
            escargots.add(escargot)
            pos = pos_finale[escargot - 1]

            if pos == start:
                min_taille = min(min_taille, len(positions))
                break
            
            if len(positions) >= min_taille:
                break
    
    return min_taille

n = int(input())
pos_finales = [int(input()) for _ in range(n)]

print(truc(n, pos_finales))