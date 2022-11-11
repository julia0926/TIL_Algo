# 실버3 ATM - https://www.acmicpc.net/problem/11399

n = int(input())
arr = list(map(int, input().split()))
arr.sort() #정렬

result = []
num = 0
for i in range(n):
    num += arr[i]
    result.append(num)

print(sum(result))
    

