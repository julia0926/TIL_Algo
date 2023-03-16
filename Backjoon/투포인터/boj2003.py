# n, m = map(int, input().split())
# arr = list(map(int, input().split()))

# result = 0
# end = 0
# interval_sum = 0

# for start in range(n):
#     while interval_sum < m and end < n:
#         interval_sum += arr[end]
#         end += 1
#     if interval_sum == m:
#         result += 1
#     interval_sum -= arr[start]

# print(result)

def solution(num, k):
    try:
        return list(str(num)).index(str(k))+1
    except:
        return -1

print(solution(123456, 7))
from 