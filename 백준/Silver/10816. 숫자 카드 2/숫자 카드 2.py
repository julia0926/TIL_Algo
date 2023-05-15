import sys
input = sys.stdin.readline
from collections import Counter
n = int(input())
piv_arr = sorted(list(map(int, input().rstrip().split())))
counter = Counter(piv_arr)

m = int(input())
arr = list(map(int, input().rstrip().split()))

for v in arr:
    print(counter[v], end=' ')