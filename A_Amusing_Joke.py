guest, residence = input(), input()
piletrouvee = input()


def truc(machin):
    occurences = {}
    for char in machin:
        if char in occurences:
            occurences[char] += 1
        else:
            occurences[char] = 1
    return occurences

occ_pile = truc(piletrouvee)
occ_necess = truc(guest + residence)

if occ_necess == occ_pile :
    print("YES")
else:
    print("NO")