from collections import deque
n, k = map(int, input().split())
arr = deque([i for i in range(1, n+1)])
result = []
piv = k-1
while arr:
    for i in range(k-1):
        arr.append(arr.popleft())
    result.append(arr.popleft())

result = str(result)
result = result.replace("[","<")
result = result.replace("]",">")
print(result)
