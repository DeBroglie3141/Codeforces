n, m, a = map(int, input().split())
print( (n//a if n%a == 0 else n//a + 1) * (m//a if m%a == 0 else m//a + 1) )