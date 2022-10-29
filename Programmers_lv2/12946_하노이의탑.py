'''
1. n-1원판을 출발 -> 중간 (재귀)
2. n원판을 출발 -> 도착
3. n-1원판을 중간 -> 도착 (재귀)

'''
# https://school.programmers.co.kr/learn/courses/30/lessons/12946
def solution(n):
    answer = []
    def hanoi(n, frm, to, mid):
        if n == 1: #이동할 원판수가 한개라면 
            answer.append([frm, to]) #이때 옮기는 경로 추가
            return
        hanoi(n-1, frm, mid, to) #1번
        answer.append([frm, to])
        hanoi(n-1, mid, to, frm)
    hanoi(n, 1, 3, 2)
    return answer

print(solution(2))