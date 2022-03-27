#실버 5 - 덱 : https://www.acmicpc.net/problem/10866
import sys
from collections import deque

n = int(input())
dq = deque()

def empty():
    if len(dq) == 0:
        return 1 
    else:
        return 0

for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "push_back":
        dq.append(order[1])
    elif order[0] == "push_front":
        dq.appendleft(order[1])
    elif order[0] == "size":
        print(len(dq))
    elif order[0] == "empty":
        print(empty())
    elif order[0] == "pop_front":
        if empty() == 1:
            print("-1")
        else:
            t = dq.popleft()
            print(t)
    elif order[0] == "pop_back":
        if empty() == 1:
            print("-1")
        else:
            t = dq.pop()
            print(t)
    elif order[0] == "front":
        if empty() == 1:
            print("-1")
        else:
            print(dq[0])
    else:
        if empty() == 1:
            print("-1")
        else:
            print(dq[len(dq)-1])