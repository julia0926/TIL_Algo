n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

chicken, house = [], []

#1. 치킨집, 집 위치 저장 
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken.append((i+1, j+1))
        elif board[i][j] == 1:
            house.append((i+1, j+1))

# 집 마다 치킨집까지의 거리 비교해서 가장 가까운 값 저장하기
def calculate(chick):
    city_chicken = 0
    for h in house:
        hx, hy = h
        distance = n*2 #최대길이 
        for cx, cy in chick:
            # print(key,value)
            piv = abs(cx-hx)+abs(cy-hy)
            distance = min(distance, piv)
        city_chicken += distance
    # print(city_chicken)
    return city_chicken


from itertools import combinations
#폐업 시킬 치킨집 m개 고르고
open_chicken = list(combinations(chicken, m)) 
result = []
for chick in open_chicken:
    result.append(calculate(chick))

print(min(result))