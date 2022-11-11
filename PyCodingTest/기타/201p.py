n, m = map(int, input().split())
arr = list(map(int, input().split()))

piv = max(arr) // 2

start = 0
end = max(arr)
result = 0

#이진탐색 
while start <= end:
    total = 0
    mid = max(start + end) // 2
    if mid >= m:
        start = mid + 1
    else:
        result = mid
        start = mid + 1

