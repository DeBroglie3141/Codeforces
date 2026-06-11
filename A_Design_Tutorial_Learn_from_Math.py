n = int(input())

def is_not_prime(n):
    for i in range(2,int(n**0.5) +1):
        if n%i == 0:
            return True
    return False

for i in range(n//2 + 1):
    if is_not_prime(i) and is_not_prime(n-i):
        print(i, n-i)
        break