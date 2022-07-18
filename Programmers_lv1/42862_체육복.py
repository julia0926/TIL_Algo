#https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    #여벌이 있어도 도난당하면 빌려줄 수 없으므로 reverse에서 제거
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    for i in set_reserve: #잃어버리지 않고, 여분이 잇는 사람들 
        if i - 1 in set_lost: #잃어버린 사람이 왼쪽에 있다면
            set_lost.remove(i-1) #빌려주고 잃어버린 집합에서 제거
        elif i + 1 in set_lost: #잃어버린 사람이 오른쪽에 있다면
            set_lost.remove(i+1)
    return n-len(set_lost) #전체 - 계산하고 남은 잃어버린 사람들

solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3], [1])
solution(3, [1,2], [2,3]) #2