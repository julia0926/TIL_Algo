#n=병사, k=무적권
#https://school.programmers.co.kr/learn/courses/30/lessons/142085

#1차 시도
def solution(n, k, enemy):
    if len(enemy) == k:
        return k
    enemy.sort(reverse=True)
    for i in range(k, len(enemy)):
        if n < enemy[i]:
            return i
        n -= enemy[i]
    
#2차시도
import heapq
def solution2(n, k, enemy):
    if len(enemy) == k:
        return k

    arr = enemy[:k] #k명을 먼저 넣고 
    heapq.heapify(arr) #정렬 시킴 
    
    for i in range(k, len(enemy)):
        heapq.heappush(arr, enemy[i]) #일단 하나씩 적을 ㄴ허고
        n -= heapq.heappop(arr) #제일 작은값(최소힙)을 남은 병사에서 제거 -> 반복
        if n < 0: #남은병사가 없다면 
            return i #해당 라운드까지므로 인덱스 리턴
            
    return len(enemy) #끝까지 왔다면 모든 라운드까지 진행됨
        

print(solution2(7, 3,[4, 2, 4, 5, 3, 3, 1]))