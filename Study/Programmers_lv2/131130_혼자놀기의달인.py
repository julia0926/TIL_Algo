#https://school.programmers.co.kr/learn/courses/30/lessons/131130

from collections import deque

#나의 풀이
def solution(cards):
    visited = [False] * len(cards)

    def bfs(start):
        arr = []
        stack = deque([start])
        while stack:
            v = stack.popleft()
            arr.append(v)
            if not visited[v-1]:
                stack.append(cards[v-1])
                visited[v-1] = True
        return arr

    result = []
    for i in range(len(cards)):
        if not visited[i]:
            visited[i] = True
            result.append(bfs(cards[i]))

    if len(result) == 1:
        return 0
    result.sort(key=len, reverse=True)
    return len(result[0]) * len(result[1])

print(solution([8,6,3,7,2,5,1,4]))
