import sys

n = int(sys.stdin.readline().strip())
arr = list(int(sys.stdin.readline().strip()) for _ in range(n))
mid = []
result = arr[:]
for i in range(max(arr)):
    mid.append(0)

for i in range(n):
    mid[arr[i]-1] += 1

for i in range(1, max(arr)):
    mid[i] += mid[i-1]
# [1, 1, 1, 2, 2, 2, 3]
for i in arr:
    result[mid[i-1]-1] = i
    mid[i-1] -= 1

for i in result:
    print(i)