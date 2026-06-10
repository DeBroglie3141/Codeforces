n = int(input())

soldiers = list(map(int, input().split()))

gsoldier, psoldier = max(soldiers), min(soldiers)
gsoldierindex, psoldierindex = soldiers.index(gsoldier), n-1-soldiers[::-1].index(psoldier)

if gsoldierindex > psoldierindex :
    print(gsoldierindex + n - 2 - psoldierindex)
else:
    print(gsoldierindex + n - 1 - psoldierindex)