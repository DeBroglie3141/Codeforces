a, b = map(int, input().split())
cmin = max(a, b) - 1

truc = 6 - cmin
machin = {1:"1/6", 2:"1/3", 3:"1/2", 4:"2/3", 5:"5/6", 6:"1/1"}

print(machin[truc])