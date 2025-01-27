from itertools import combinations
n, m = map(int, input().split())
arr = list(map(int, input().split()))

combi = list(combinations(arr, 3))
# print(combi_sum)
result = 0
for val in combi:
    if result < sum(val) <= m:
        result = sum(val)

print(result)


    
