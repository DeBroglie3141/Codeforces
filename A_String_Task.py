phrase = input().lower()
sortie = ''

for char in phrase:
    if char not in {'a', 'e', 'i', 'o', 'u', 'y'}:
        sortie += '.' + char

print(sortie)