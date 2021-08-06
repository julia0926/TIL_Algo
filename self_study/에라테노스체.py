n = 100
a = [False,False] + [True]*(n-1)
primes = []

for i in range(2, n+1): #n까지임 
    if a[i]: #값이 들어있으면 
        primes.append(i)
        # 2*i 인 이유는 그 값 이후의 두배 값부터 시작해야되므로 
        for j in range(2*i, n+1, i): #2*i~n+1까지 i만큼
            a[j] = False
print(primes)
 