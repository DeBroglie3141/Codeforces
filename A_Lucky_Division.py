n = input()
nbr_chanceux = {4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777}

def truc(n):
    if all(chiffre in {'4', '7'} for chiffre in n):
        return "YES"
    else:
        n = int(n)
        for nbr in nbr_chanceux:
            if n%nbr == 0:
                return "YES"
        return "NO"

print(truc(n))