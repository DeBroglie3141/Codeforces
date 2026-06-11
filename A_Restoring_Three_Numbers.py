nbrs = sorted(list(map(int, input().split())))[::-1]

abc = nbrs[0]
ab, ac, bc = nbrs[1], nbrs[2], nbrs[3]

print(abc - ab, abc - bc, abc - ac)