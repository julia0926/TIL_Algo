# https://www.acmicpc.net/problem/1406
'''
L : 왼쪽 한칸 이동
D : 오른쪽 한칸 이동
B : 왼쪽 문자 삭제
P $ : $라는 문자를 커서 왼쪽에 추가 
초기커서는 맨뒤에
구현 -> 커서기준 왼쪽 오른쪽 배열을 나누어서 구현함 
'''
import sys
from collections import deque

string = list(input())
N = int(sys.stdin.readline())

deq = deque()
temp = deque()

deq.extend(string)

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "L":
        if len(deq) != 0:
            temp.appendleft(deq.pop())
    elif command[0] == "D":
        if len(temp) != 0:
            deq.append(temp.popleft())
    elif command[0] == "B":
        if len(deq) != 0:
            deq.pop()
    elif command[0] == "P":
        deq.append(command[1])

print("".join(deq) + "".join(temp))