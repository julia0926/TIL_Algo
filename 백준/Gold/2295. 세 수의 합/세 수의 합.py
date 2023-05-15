import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

two = set()
for i in range(n):
    for j in range(i, n):
        two.add(arr[i]+arr[j])

result = 0
for i in range(n):
    for j in range(i+1, n):
        diff = arr[j] - arr[i]
        if diff in two:
            result = max(result, arr[j])
            break
print(result)