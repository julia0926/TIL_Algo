import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().strip().split()))

total = [sum(arr[:k])]
result = -101
for i in range(1, len(arr)-k+1):
    result = total[-1] + arr[i+k-1] - arr[i-1]
    total.append(result)
print(max(total))