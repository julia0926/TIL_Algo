import sys
input = sys.stdin.readline
from bisect import bisect_left
n = int(input())
arr = list(map(int, input().rstrip().split()))
sort_arr = sorted(arr)
#중복제거
# new_arr = [sort_arr[0]]
# for i in range(1, n):
#     if new_arr[-1] != sort_arr[i]:
#         new_arr.append(sort_arr[i])
# print(new_arr)
new_arr = sorted(list(set(sort_arr)))
result = []
for val in arr:
    n = bisect_left(new_arr, val)
    result.append(n)
print(*result)