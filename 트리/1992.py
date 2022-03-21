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
half = (N // 2) - 1
result = ""

def recursive(x, y, n):
    first = area[x][y] #재귀 첫번째 값 
    for i in range(x):
        for j in range(y):
