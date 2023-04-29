n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
piv = list(map(int, input().split()))

ans = []
# -10,2,3,6,10

from bisect import bisect_left

res = []
for p in piv:
    idx = bisect_left(card, p)
    if idx < len(card) and card[idx] == p:
        res.append(1)
    else:
        res.append(0)

print(*res)