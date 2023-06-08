import sys
input = sys.stdin.readline

h, w = map(int, input().rstrip().split())
rain = list(map(int, input().strip().split()))
result = 0
#최대 높이 찾기
for i in range(1, w-1): #가장 왼쪾과 오른쪽은 고일 수 없음
    left = max(rain[:i])
    right = max(rain[i+1:])
    # print(left, right)
    piv = min(left, right)
    if rain[i] < piv:
        result += piv - rain[i]

print(result)