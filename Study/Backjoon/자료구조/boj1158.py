#https://www.acmicpc.net/problem/1158
from collections import deque

n, k = map(int, input().split())

arr = list(i for i in range(1, n+1))
answer = [] 
idx = 0 #제거될 인덱스 

for i in range(n):
    idx += (k-1) #처음은 인덱스가 0부터 시작해서, 나머지는 하나씩 빼야하니까 -1함
    if idx >= len(arr):
        idx %= len(arr)
    answer.append(arr[idx])
    del arr[idx]
print(str(answer).replace('[', '<').replace(']','>'))