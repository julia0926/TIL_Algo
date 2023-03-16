#https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations

def solution(k, dungeons):
    piv = [i for i in range(len(dungeons))]
    permu = list(permutations(piv, len(dungeons)))
    max_list = []
    
    for orders in permu:
        count = 0
        piro = k
        for order in orders:
            if piro - dungeons[order][0] < 0: #최소 피로도보다 크다면 탐험불가
                max_list.append(count)
                break
            else: #탐험할 수 있다면 
                piro = piro - dungeons[order][1] #남은 피로도를 계속 갱신
                count += 1
        if count == len(dungeons): #던전 길이만큼 탐험 할 수 있는 경우에도
            max_list.append(count) #count 추가
     
    return max(max_list)

print(solution(80, [[80,20],[50,40],[30,10]]))