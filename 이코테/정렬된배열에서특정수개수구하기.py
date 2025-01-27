from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

a, b = bisect_left(arr, x), bisect_right(arr, x)
print(b-a)