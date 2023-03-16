#골드 5 : 치킨 배달 https://www.acmicpc.net/problem/15686

from itertools import combinations
'''
1. 치킨집을 M개 고르고 -> 조합으로 
2. 한개씩 치킨집 - 도시 거리 구함
3. 총합 값을 더해서 프린트함 
'''
N, M = map(int, input().split())
chicken, house = [], []

for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] == 2:
            chicken.append((i, j))
        elif arr[j] == 1:
            house.append((i, j))
combi_chick = list(combinations(chicken, M))

#한 집에 치킨거리 구하기 
def get_sum(chick):
    house_dis = 0
    for hx, hy in house:
        distance = []
        for cx, cy in chick:
            distance.append(abs(hx-cx) + abs(hy-cy))
        house_dis += min(distance)
    return house_dis

result = []
#도시의 치킨거리 구하기 
for i in combi_chick:
    result.append(get_sum(i))
print(min(result))
