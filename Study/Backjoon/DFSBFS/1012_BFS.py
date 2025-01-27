from collections import deque
from itertools import permutations

# 방향 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 사용해 특정 위치에서 다른 모든 위치까지의 최단 거리를 계산하는 함수
def bfs(start, plan, n, m):
    queue = deque([start])
    visited = [[-1] * m for _ in range(n)]
    visited[start[0]][start[1]] = 0
    distances = {}

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and plan[nx][ny] != '#':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                if plan[nx][ny] == '*' or plan[nx][ny] == '.':
                    distances[(nx, ny)] = visited[nx][ny]
    
    return distances

def solution(plan):
    n, m = len(plan), len(plan[0])
    
    # 시작 지점과 청소 지점(*의 위치) 찾기
    start = []
    points = []
    for i in range(n):
        for j in range(m):
            if plan[i][j] == '*':
                points.append((i, j))  # 청소해야 할 지점
            elif plan[i][j] == '.':
                start.append((i, j))  # 시작 지점

    # 시작점 또는 청소 지점이 없으면 0 리턴
    if not points or not start:
        return 0

    # 모든 시작 지점에서 청소 지점 사이의 최단 거리 계산
    all_distances = {}
    for s in start:
        distances_from_start = bfs(s, plan, n, m)  # 시작 지점에서 청소 지점까지의 거리 계산
        all_distances[s] = {p: distances_from_start[p] for p in points if p in distances_from_start}
        print(s, all_distances[s])
    # print(f"All distances from start points: {all_distances}")  # 거리 확인용 출력
    
    # 순열을 통해 모든 청소 순서를 고려한 최소 이동 횟수 계산
    # min_steps = float('inf')
    # for s in start:  # 모든 시작 지점에 대해
    #     for perm in permutations(points):  # 청소 지점들에 대한 순열 생성
    #         current_steps = 0
    #         current_point = s  # 시작 지점에서 시작
    #         for next_point in perm:  # 청소 지점으로 이동
    #             # 시작점에서 청소 지점까지의 거리만 계산 (올바른 시작 지점으로 조회)
    #             if next_point in all_distances[current_point]:
    #                 current_steps += all_distances[current_point][next_point]
    #                 current_point = next_point
    #             else:
    #                 current_steps = float('inf')
    #                 break
    #         min_steps = min(min_steps, current_steps)

    # return min_steps if min_steps != float('inf') else 0

# BFS 함수는 동일하게 유지됩니다.


# 테스트 케이스 실행
plan1 = [
    ".*#..*",
    ".*#*.#",
    "######",
    ".*..#.",
    "...###"
]

plan2 = [
    '*#..',
    '#..#', 
    '.##.', 
    '...*'
]

# print(solution(plan1))  # 예상 출력: (모든 시작점에서 모든 청소 지점으로의 최단 거리)
print(solution(plan2))  # 예상 출력: (모든 시작점에서 모든 청소 지점으로의 최단 거리)

