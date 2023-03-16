# 브2 시험감독 : https://www.acmicpc.net/problem/13458
import sys
n = int(input())
a = list(map(int,sys.stdin.readline().split()))
b, c = map(int,sys.stdin.readline().split())
cnt = 0

for val in a:
    val -= b        
    cnt += 1
    if val > 0:
        cnt += val // c
        if val % c != 0:
            cnt += 1
        
        

print(cnt)