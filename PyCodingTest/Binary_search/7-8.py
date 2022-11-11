
n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

start = 0
end = max(arr)
result = 0

while start <= end:
    mid = (start+end) // 2 #높이 
    sum_val = 0
    for val in arr:
        if val > mid: #기준이 값들보다 작으면 
            sum_val += val - mid
    
    if sum_val < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
        


        


