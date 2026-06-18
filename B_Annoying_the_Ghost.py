import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        b = [int(next(it)) for _ in range(n)]
        used = [False] * n
        assigned = [None] * n
        possible = True
        for i in range(n):
            ai = a[i]
            found = -1
            for j in range(n):
                if not used[j] and b[j] >= ai:
                    found = j
                    break
            if found == -1:
                possible = False
                break
            used[found] = True
            assigned[i] = found
        if not possible:
            out_lines.append("-1")
            continue
        inv = 0
        # count inversions in assigned positions
        for i in range(n):
            aj = assigned[i]
            for k in range(i + 1, n):
                if assigned[k] < aj:
                    inv += 1
        out_lines.append(str(inv))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
