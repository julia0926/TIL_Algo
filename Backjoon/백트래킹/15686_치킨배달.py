#https://www.acmicpc.net/problem/15686

from itertools import combinations


n, m = map(int, input().split())

house, chicken = [], []

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 1: house.append((i, j))
        elif arr[j] == 2: chicken.append((i, j))

#[(0, 2), (1, 4), (2, 1), (3, 2)] [(1, 2), (2, 2), (4, 4)]
combi_chick = list(combinations(chicken, m)) #치킨집 조합을 해야지만, 최대 m개를 택함.

