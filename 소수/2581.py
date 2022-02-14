n = int(input())
m = int(input())

primes = []

for i in range(n, m+1):
    cnt = 1
    for j in range(2, i):
        if i % j == 0:
            cnt = 0
    if cnt and i != 1:
        primes.append(i)

if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)
