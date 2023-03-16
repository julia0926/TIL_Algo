#https://www.acmicpc.net/problem/21313

n = int(input())
answer = ""
if n % 2 == 0:
    answer = [1,2]*(n//2)
else:
    answer = ([1,2]*(n//2))+[3]

print(*answer)
    

