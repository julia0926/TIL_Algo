n = int(input())
m = int(input())

a = [False, False] + [True] * (m-1)
primes = []

for i in range(2, m+1):
    if a[i]: primes.append(i)
    for j in range(2*i, m+1, i):
        a[j] = False

sum_v = 0
min_v = 1e9
for i in range(n, m+1):
    if i in primes:
        sum_v += i
        min_v = min(min_v, i)

if sum_v == 0:
    print(-1)
else:
    print(sum_v)
    print(min_v)    
