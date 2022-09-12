# https://school.programmers.co.kr/learn/courses/30/lessons/87390

'''
이 문제의 핵심은 단순히 전체 배열을 구하는 것이 아닌
각 위치와 n과의 관계를 잘 파악해서 계산하는 것
예를 들어 n=3인데, 
index 5의 위치 값을 구하려면
몫: 5//3 = 1
나머지: 5%3= 2
둘 중 큰값인 2에 +1를 더해 해당 위치의 값은 3이된다.
'''
def solution(n, left, right):
    #시간초과 !! 
    answer = []
    for i in range(left, right+1):
        answer.append(max(i//n, i%n)+1)
    return answer


print(solution(3,2,5))
solution(4,7,14)