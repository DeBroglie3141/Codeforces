t = int(input())

for _ in range(t):
    n =  input()[::-1]
    len_n = len(n)
    round_terms = []
    for i in range(len_n):
        chiffre = n[i]
        if chiffre != "0":
            round_terms.append(int(chiffre)*(10**i))
    print(len(round_terms))
    print(*round_terms)