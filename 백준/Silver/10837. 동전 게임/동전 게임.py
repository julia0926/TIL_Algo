#참고풀이 : https://mygumi.tistory.com/305
import sys
input = sys.stdin.readline

k = int(input()) #라운드수
c = int(input()) #입력 개수
for i in range(c):
    m, n = map(int, input().split()) 
    gap = abs(m-n)
    remain = k - max(m,n)
    if m == n:
        print("1")
    elif m < n:
        if gap - remain  <= 1:
            print("1")
        else:
            print("0")
    else: #m > n
        if gap - remain  <= 2: #영희가 먼저 시작하니까 하나 더줌
            print("1")
        else:
            print("0")
    

