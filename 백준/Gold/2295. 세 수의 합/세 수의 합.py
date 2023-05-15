import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)])
two_arr = [] #x+y를 미리 다 계산해서 배열에 저장
for i in range(n):
    for j in range(i, n):
        two_arr.append(arr[i]+arr[j])
two_arr.sort()
result = 0
#x+y = z-k 임을 생각해서 구현한다.

for i in range(n): #k 최종의 값
    for j in range(i+1, n): #z 값
        diff = arr[j]-arr[i] #z-k 값
        start, end = 0, len(two_arr)-1
        #이분 탐색 = two_arr(x+y)의 배열에서 z-k 값이 있는지 이분탐색으로 찾는다.
        while start <= end:
            mid = (start+end)//2
            mid_val = two_arr[mid]
            if diff > mid_val:
                start = mid + 1
            elif diff < mid_val:
                end = mid - 1
            elif diff == mid_val:
                result = max(result, arr[j])
                break

print(result)
