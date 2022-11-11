# https://www.acmicpc.net/problem/2003

n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
interver_sum = 0
end = 0

for start in range(n):
    while interver_sum < m and end < n:
        interver_sum += arr[end]
        end += 1

    if interver_sum == m:
        count += 1
    interver_sum -= arr[start]
    
    
print(count)