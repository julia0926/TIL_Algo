from itertools import combinations

n, m = map(int, input().split())
arr = sorted(list(input().split()))
vowels = ['a','e','i','o','u']
result = []

for c in combinations(sorted(arr), n):
    result.append(''.join(c))

#1개 모음, 2개 자음 거르기
for res in result:
    cnt = sum(res.count(v) for v in vowels)
    if cnt >= 1 and n - cnt >= 2:
        print(res)
