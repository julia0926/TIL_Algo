#https://school.programmers.co.kr/learn/courses/30/lessons/135808

'''
낮은점수 : p
한 상자 가격 : p*m
'''
#내풀이
def solution(k, m, score):
    start = 0
    answer = 0
    arr = sorted(score, reverse=True)
    for i in range(1, (len(score)//m)+1):
        answer += min(arr[start:i*m]) * m
        start = i*m
    return answer

solution(3,4, [1, 2, 3, 1, 2, 3, 1])
solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]	)

'''
개선점: start를 없앨수 없을까?
참고 : 아예 시작을 부분 배열의 끝으로 시작해서 
'''
def solution2(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(m-1, len(score), m):
        answer += score[i] * m 
        print(score[i], score, i)
    return answer

print(solution2(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]	))
