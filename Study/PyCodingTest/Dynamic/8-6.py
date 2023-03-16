n = int(input())
store = list(map(int, input().split()))
d = [0] * 100 

d[0] = store[0]
d[1] = max(d[0], store[1])

for i in range(2, n): #창고가 i개 있다고 할 때 
    d[i] = max(d[i-1], d[i-2] + store[i])

print(d[n-1])