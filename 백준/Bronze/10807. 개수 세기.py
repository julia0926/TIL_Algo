from bisect import bisect_left, bisect_right

n = int(input())
arr = list(map(int, input().split()))
v = int(input())

arr.sort()

val = bisect_right(arr, v) - bisect_left(arr, v)
print(val)


