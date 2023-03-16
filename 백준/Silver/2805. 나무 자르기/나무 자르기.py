n, m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, max(arr)
result = 0

while start<=end:
    total = 0
    mid = (start+end)//2
    #양수만 집에 가져갈수 있음
    for a in arr:
        if a-mid > 0:
            total += a-mid #자른 나무들 합
            
    if total >= m: #더 크면 자를 수 있따.
        #일단 최소값 저장해둠 왜냐? m이 꼭 아닐수도 잇어. 최소 m미터이기 때문에 m 이상일 수도 있음
        result = mid 
        start = mid +1
    else: #작으면 값을 구할 수 없으므로 end값을 내림
        end = mid - 1

print(result)

