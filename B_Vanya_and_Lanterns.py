n, l = map(int, input().split())
lanterns = sorted(list(map(int, input().split())))

min_diameter = max(2*lanterns[0], 2*(l-lanterns[-1]))

for i in range(n-1):
    min_diameter = max(min_diameter, lanterns[i+1] - lanterns[i])

print(min_diameter / 2)