n, m = map(int,input().split())
x, y, direction = map(int,input().split())
visited = [[0] * m for _ in range(n)] # 방문여부
visited[x][y] = 1 #현재 위치는 방문 

game_map = []
for k in range(n):
    game_map.append(list(map(int,input().split())))

# 바다는 갈수 없음. 육지만 이동 가능
# 북 서 남 동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1: #북->서쪽으로 
        direction = 3

count = 1 # 캐릭터가 방문한 칸 수
turn_num = 0 # 몇 번 돌았는지

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #왼쪽 방향에 가보지 않은 칸이 존재 
    if game_map[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_num = 0
        continue
    #왼쪽 방향에 가보지 않은 칸이 없다면 
    else:
        turn_num += 1
    #네 방향 모두 돌았을 때 한 칸 뒤로 돌아감 
    if turn_num == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤쪽 방향이 바다인 경우 움직일 수 없음
        if game_map[nx][ny] == 1:
            break
        #육지이면 그대로 뒤로 옮김
        else:
            x, y = nx, ny
        #다시 1단계로 돌아가므로 몇 번 돌았는 지 변수도 0으로 
        turn_num = 0

print(count)



