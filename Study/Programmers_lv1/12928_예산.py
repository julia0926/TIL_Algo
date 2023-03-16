# answer : 최대 몇개의 부서에 물품을 지원 

def solution(d, budget):
    answer = 0
    sort_d = sorted(d)
    for value in sort_d:
        budget -= value
        if budget < 0:
            break
        answer += 1 
    return answer

print(solution([1,3,2,5,4], 9))
print("-" * 10)
print(solution([2,2,3,3], 10))