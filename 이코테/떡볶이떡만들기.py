n, m = map(int, input().split()) #떡의 개수, 요청한 떡의 길이
arr = list(map(int, input().split()))
'''
4 6
19 15 10 17
'''
start = 0
end = max(arr)

result = 0
while start <= end:
    total = 0
    mid = (start+end)//2
    for num in arr:
        if num - mid > 0:
            total += (num-mid)
    
    if total >= m:
        start = mid + 1
        result = mid #최대한 덜 짤랐을 때니까 기록해둔다..!
    else:
        end = mid - 1

print(result)

