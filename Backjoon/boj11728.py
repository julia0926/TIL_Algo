n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = [0] * (len(a)+len(b))
a_idx, b_idx = 0, 0

for i in range(len(result)):
    if a[a_idx] <= b[b_idx]: result[i] = a[a_idx]