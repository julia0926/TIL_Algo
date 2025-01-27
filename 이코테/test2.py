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
    
    # 모든 청소 지점(*의 위치) 찾기
    points = []
    for i in range(n):
        for j in range(m):
            if plan[i][j] == '*':
                points.append((i, j))
    print(points)
    # # 시작 지점이 없으면 바로 0 리턴
    # if not points:
    #     return 0
    # print(points)
    # # 모든 청소 지점 간의 거리 계산
    # distances_between_points = {}
    
    # # 각 청소 지점 간의 최단 거리 계산
    # for point in points:
    #     distances = bfs(point, plan, n, m)
    #     distances_between_points[point] = distances

    # # 모든 청소 지점 순열을 구해서 최소 이동 거리를 계산
    # min_distance = float('inf')
    
    # for perm in permutations(points[1:]):  # 첫 번째 지점은 고정하고 나머지 순열
    #     current_distance = 0
    #     current_position = points[0]
        
    #     for next_position in perm:
    #         if next_position not in distances_between_points[current_position]:
    #             current_distance = float('inf')
    #             break
    #         current_distance += distances_between_points[current_position][next_position]
    #         current_position = next_position
        
    #     min_distance = min(min_distance, current_distance)
    
    # # 만약 갈 수 없는 경로가 있으면 -1 리턴
    # return min_distance if min_distance != float('inf') else -1

# 테스트 케이스 실행
plan1 = [
    ".*#..*",
    ".*#*.#",
    "######",
    ".*..#.",
    "...###"
]

plan2 = ['*#..', '#..#', '.##.', '...*']

print(solution(plan1))  # 예상 출력: 3
print(solution(plan2))  # 예상 출력: 2
