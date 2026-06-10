n = int(input())
points = list(map(int, input().split()))
count = 0
bestperf, worstperf = points[0], points[0]

for score in points :
    if score < worstperf :
        worstperf = score
        count += 1
    elif score > bestperf :
        bestperf = score
        count += 1

print(count)