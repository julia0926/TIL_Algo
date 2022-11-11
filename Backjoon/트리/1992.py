#실버1 - 쿼드트리 : https://www.acmicpc.net/problem/1992

import sys
input = sys.stdin.readline

N = int(input())
area = [list(map(int, input().strip())) for _ in range(N)]

'''
일단 4분할 한 영역의 결과 값 확인 
재귀 시작전 [
재귀 끝나면 ]
'''
result = []

def recursive(x, y, n):
    first = area[x][y] #재귀 첫번째 값 
    for i in range(x, x+n):
        for j in range(y, y+n):
            if first != area[i][j]:
                half = n // 2
                result.append('(')
                recursive(x, y, half) #1사분면
                recursive(x, y+half, half) #2사분면
                recursive(x+half, y, half)#3사분면
                recursive(x+half, y+half, half) #4사분면
                result.append(')')
                return
    
    if first == 0:
        result.append('0')
    else:
        result.append('1')

recursive(0, 0, N)
for k in result:
    print(k, end='')