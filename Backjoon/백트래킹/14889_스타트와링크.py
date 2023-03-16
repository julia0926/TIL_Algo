#https://www.acmicpc.net/problem/14889
from itertools import combinations


n = int(input())

# arr = list(list(map(int, input().split())) for _ in range(n))
combi = list(combinations(range(1, n+1),n//2))
print(combi)