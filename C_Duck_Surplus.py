import sys

def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        st = []
        for _ in range(n):
            x = int(next(it))
            st.append(x)
            while len(st) >= 2 and st[-2] > st[-1]:
                y = st.pop()
                x = st.pop()
                st.append(y)
                st.append(x + y)
        out_lines.append(str(max(st)))
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
