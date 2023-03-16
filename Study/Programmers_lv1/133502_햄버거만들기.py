#https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    hambuger = [1,2,3,1]
    tmp = []
    answer = 0
    for i in ingredient:
        tmp.append(i)
        if tmp[-4:] == hambuger:
            answer += 1
            for i in range(4):
                tmp.pop()
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))