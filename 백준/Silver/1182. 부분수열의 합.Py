from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for i in range(1, n+1):
    print(list(map(list, combinations(arr, i))))
    for sum_val in list(map(list, combinations(arr, i))):
        if s == sum(sum_val):
            result += 1

print(result)