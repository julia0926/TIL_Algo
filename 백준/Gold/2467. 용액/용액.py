import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

if arr[0] >= 0:
    print(arr[0], arr[1])
elif arr[-1] <= 0:
    print(arr[-2], arr[-1])
else:
    left, right = 0, n-1
    a, b = 0, 0
    min_val = sys.maxsize

    while left < right:
        sum_v = arr[left] + arr[right]
        if abs(sum_v) < min_val:
            a, b = left, right
            min_val = abs(sum_v)
        # print(left, right, abs(sum_v))
        
        if sum_v < 0:
            left += 1
        elif sum_v > 0:
            right -= 1
        else: #0이라면
            break
    print(arr[a], arr[b])


