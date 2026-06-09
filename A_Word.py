word = input()

count = 0
for letter in word:
    if letter.isupper() :
        count += 1

if count > len(word)/2 :
    print(word.upper())
else:
    print(word.lower())