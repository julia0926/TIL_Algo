#https://www.acmicpc.net/problem/20152
h, n = map(int, input().split()) #집, pc방 

if h == n:
    print(1)

answer = abs(h - n)**2
print(answer)
piv = (answer - (h - n)) // 2
print(piv-1)
