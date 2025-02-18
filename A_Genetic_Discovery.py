N = int(input())
genes = [input() for _ in range(N)]

len_genes = len(genes[0])
gene_final = ['.'] * len_genes

def test(i):
    for gene in genes:
        machin = gene[i]
        if (machin != '.') and (machin != truc):
            return False
    return True

def machin(i):
    for gene in genes:
        if gene[i] != '.':
            return gene[i]
    return '.'

for i in range(len_genes):
    truc = machin(i)
    if test(i):
        gene_final[i] = truc

print(''.join(gene_final))
