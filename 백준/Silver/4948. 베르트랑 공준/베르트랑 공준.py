import sys, math
input = sys.stdin.readline
max_v = 123456 * 2
arr = [True for _ in range(max_v)]

for k in range(2, int(math.sqrt(max_v))+1):
    if arr[k]: #소수라면 
        for j in range(k*2, max_v, k):
            arr[j] = False

def calculate(n):
    result = 0
    for i in range(n+1, (2*n)):
        if arr[i]:
            result+= 1
    print(result)

while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        calculate(n)