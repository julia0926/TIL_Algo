n = int(input())

arr = [0 for _ in range(n+1)]

for i in range(n+1):
    if i == 0 or i == 1:
        arr[i] = i
    else:
        arr[i] = arr[i-1] + arr[i-2]

print(arr[n])