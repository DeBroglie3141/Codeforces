a, b, c = map(int, [input() for _ in range(3)])

res1 = a + b + c
res2 = a * b * c
res3 = (a + b) * c
res4 = a * (b + c)

print(max(res1, res2, res3, res4))