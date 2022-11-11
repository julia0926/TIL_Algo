# https://www.acmicpc.net/problem/11728
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result_arr = []

i, j, k = 0, 0, 0
for _ in range(n+m):
     #arr2의 배열이 없거나, 첫번째 배열의 값이 더 작을때
    if j >= m or (i < n and arr[i] <= arr2[j]):
        result_arr.append(arr[i])
        i += 1
    else:
        result_arr.append(arr2[j])
        j+=1
    
print(*result_arr)