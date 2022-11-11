import sys
input = sys.stdin.readline #한줄 단위로 입력받기때문에 개행문자 제거

n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]
result = []

def quadtree(x, y, n):
    data = arr[x][y]
    for i in range(x, x+n): #처음엔 1~7까지 비교, 다른 값 나오면 쪼개서 비교 
        for j in range(y, y+n):
            if data != arr[i][j]: # 다른 값이 발견된다면 !
                val = n//2
                result.append('(')
                quadtree(x, y, val) #1사분면
                quadtree(x, y+val, val) #2사분면
                quadtree(x+val, y, val) #3사분면
                quadtree(x+val, y+val, val) #4사분면 
                result.append(')')
                return #어짜피 재귀호출 하므로 한번 다른 값이 발견되면 더이상 반복 X
    #다른값이 발견되지 않을 때 
    if data == 0: 
        result.append('0')
    else:
        result.append('1')

quadtree(0,0,n)
for k in result:
    print(k,end='') #엔터 넘기지 않기 위해


        