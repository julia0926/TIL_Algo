import sys
input = sys.stdin.readline

n = int(input())
piv_arr = sorted(list(map(int, input().rstrip().split())))
m = int(input())
arr = list(map(int, input().rstrip().split()))


def mid_path(piv): #이분 탐색
    start, end = 0, n-1
    while start <= end:
        mid = (start+end)//2
        if piv_arr[mid] < piv:
            start = mid + 1
        elif piv_arr[mid] > piv:
            end = mid - 1
        elif piv_arr[mid] == piv:
            return 1
    return 0

for val in arr:
    print(mid_path(val))
