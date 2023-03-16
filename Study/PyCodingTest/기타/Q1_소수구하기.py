from os import pread


m, n = map(int, input().split())
prime = [False, False] + [True] * (n-1)
result = []

for i in range(2, n+1):
    if prime[i]:
        for j in range(i*2, n+1, i):
            prime[j] = False
        if i >= m:
            result.append(i)

for i in result:
    print(i)