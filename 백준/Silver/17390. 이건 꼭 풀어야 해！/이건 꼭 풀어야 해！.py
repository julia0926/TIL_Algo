import sys
input = sys.stdin.readline
n, q = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
sum_val = [0] * (n+1)

for i in range(n):
    sum_val[i] = sum_val[i-1]+arr[i]
    

for i in range(q):
    a, b = map(int,input().split())
    print(sum_val[b-1]-sum_val[a-2])
