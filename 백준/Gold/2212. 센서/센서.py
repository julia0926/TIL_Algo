n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()

diff = []
for i in range(len(arr)-1):
    diff.append(arr[i+1]-arr[i])

print(sum(sorted(diff, reverse=True)[k-1:]))