from itertools import combinations
from math import comb
# combi : [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

n = int(input())
soccor = list(list(map(int, input().split())) for _ in range(n))
list_n = list(i for i in range(n))
combi = list(combinations(list_n, n // 2))

power_list = []

min_gap = 1e9

for i in range(len(combi) // 2):
    team = combi[i]
    start_score = 0
    for j in range(n // 2):
        member = team[j]
        for k in team:
            start_score += soccor[member][k]

    team = combi[-i-1]
    link_score = 0
    for j in range(n // 2):
        member = team[j]
        for k in team:
            link_score += soccor[member][k]

    min_gap = min(min_gap, abs(start_score - link_score))

print(min_gap)




# 하다가 실패 
# power_list = list(set(power_list)) #중복 값 제거 
# print(power_list)
# min_val = 1e9 #제일 큰수 

# for i in range(len(power_list)):
#     for k in range(i+1, len(power_list) - 1):
#         gap = abs(power_list[i] - power_list[k])
#         print(f'{power_list[i]} - {power_list[k]} = {gap}')
#         if min_val > gap:
#             min_val = gap
#             if gap == 0:
#                 break
            

# print(min_val)