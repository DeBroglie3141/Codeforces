n = int(input())
truc = input()
last = truc[0]
machin = 0

for i in range(1,n):
    if last == truc[i] :
        machin += 1
    else :
        last = truc[i]

print(machin)