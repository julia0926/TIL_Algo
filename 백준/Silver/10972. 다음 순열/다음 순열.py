import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

for i in range(n-1, 0, -1):
    if arr[i-1] < arr[i]:
        for j in range(n-1, 0, -1):
            if arr[i-1] < arr[j]:
                arr[i-1], arr[j] = arr[j], arr[i-1]
                result = arr[:i] + sorted(arr[i:])
                print(" ".join(map(str, result)))
                exit(0)
print(-1)
        


