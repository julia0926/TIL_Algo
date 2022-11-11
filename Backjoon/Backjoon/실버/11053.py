# 실버2 - 가장 긴 증가하는 부분 수열 : https://www.acmicpc.net/problem/11053

n = int(input())
arr = list(map(int, input().split()))
cnt = 1
tmp = []
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        tmp.append(arr[i+1])
        arr.remove(arr[i+1])
    else: