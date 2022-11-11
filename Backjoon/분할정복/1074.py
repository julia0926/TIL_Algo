N, r, c = map(int,input().split())
count = 0
def zway(x ,y ,n):
    global count
    n = n // 2
    if n==1: #2X2 배열일 때 
        if x==r and y==c: #예제 배열 기준으로 0
            print(count)
            return
        count+=1
        if x+1==r and y==c: #1
            print(count)
            return
        count+=1
        if x==r and y+1==c: #2
            print(count)
            return
        count+=1
        if x+1==r and y+1==c: #3
            print(count)
            return
        count+=1
    else: 
        #탐색
        zway(x, y ,n) #1사분면
        zway(x, y+n, n) #2사분면
        zway(x+n, y, n) #3사분면
        zway(x+n, y+n, n) #4사분면 

zway(0,0,2 ** N)

