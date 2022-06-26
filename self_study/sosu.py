n = int(input())

isPrime = [False, False] + [True] * (n-1)
sosu = []
for i in range(2, n+1):
    if isPrime[i]:
        sosu.append(i)
        for j in range(i*2, n+1, i):
            isPrime[j] = False

print(sosu)