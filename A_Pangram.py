n = int(input())

sentence = input().lower()

if len(set(sentence)) == 26:
    print("YES")
else:
    print("NO")