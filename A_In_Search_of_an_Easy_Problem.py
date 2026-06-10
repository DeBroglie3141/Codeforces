n = int(input())
avis = list(map(int, input().split()))

def truc(avis):
    for machin in avis:
        if machin == 1:
            return "HARD"
    return "EASY"

print(truc(avis))