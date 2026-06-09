import sys
from collections import defaultdict

def main():
    input = sys.stdin.buffer.read().split()
    idx = 0
    t = int(input[idx]); idx += 1
    
    out = []
    for _ in range(t):
        n, m = int(input[idx]), int(input[idx+1]); idx += 2
        
        # Lire la grille à plat (une seule liste)
        size = n * m
        flat = input[idx:idx+size]
        idx += size
        
        # color_adjacent[c] = True si la couleur c a deux voisins
        # On utilise deux tableaux pour éviter defaultdict overhead
        # Les couleurs vont de 1 à n*m
        max_color = size + 1
        seen      = bytearray(max_color)  # couleur déjà rencontrée ?
        adjacent  = bytearray(max_color)  # couleur avec deux voisins ?
        
        cells = [int(x) for x in flat]
        
        # Vérifier voisins horizontaux
        for i in range(n):
            base = i * m
            for j in range(m - 1):
                a = cells[base + j]
                b = cells[base + j + 1]
                if a == b:
                    adjacent[a] = 1
        
        # Vérifier voisins verticaux
        for i in range(n - 1):
            base = i * m
            for j in range(m):
                a = cells[base + j]
                b = cells[base + m + j]
                if a == b:
                    adjacent[a] = 1
        
        # Marquer les couleurs présentes
        for c in cells:
            seen[c] = 1
        
        total = 0
        best_saving = 0
        for c in range(1, max_color):
            if seen[c]:
                cost = 2 if adjacent[c] else 1
                total += cost
                if cost > best_saving:
                    best_saving = cost
        
        out.append(total - best_saving)
    
    sys.stdout.write('\n'.join(map(str, out)) + '\n')

main()