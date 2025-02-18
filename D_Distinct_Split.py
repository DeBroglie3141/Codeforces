import sys

def max_distinct_split(n, s):
    prefix_set = set()
    prefix_count = [0] * n
    
    for i in range(n):
        prefix_set.add(s[i])
        prefix_count[i] = len(prefix_set)

    suffix_set = set()
    suffix_count = [0] * n

    for i in range(n - 1, -1, -1):
        suffix_set.add(s[i])
        suffix_count[i] = len(suffix_set)

    max_value = 0
    for i in range(n - 1):
        max_value = max(max_value, prefix_count[i] + suffix_count[i + 1])

    return max_value

def truc():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        s = data[index + 1]
        index += 2
        results.append(str(max_distinct_split(n, s)))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    truc()
