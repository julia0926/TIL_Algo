from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

combi = list(combinations(cards,3))
# print(combi)
max_val = 0
for tup in combi:
    sum_val = sum(list(tup))
    if max_val < sum_val <= m:
        max_val = sum_val
        #print(max_val)

print(max_val)