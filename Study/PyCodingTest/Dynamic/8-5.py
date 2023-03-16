n = int(input())
arr = [0] * n+1 #연산의 횟수

for i in range(2, n+1):
    #1로 뺀 경우
    arr[i] = arr[i-1] + 1
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i//2])
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i//3])
    if i % 5 == 0:
        arr[i] = min(arr[i], arr[i//5])

