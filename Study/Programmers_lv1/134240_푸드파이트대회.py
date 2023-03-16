#https://school.programmers.co.kr/learn/courses/30/lessons/134240

#내풀이
def solution(food):
    answer = ""
    #for문 두개 
    for i in range(len(food)):
        if food[i] != 0 and food[i] // 2 > 0:
            for _ in range(food[i]//2):
                answer += str(i)
            
    copy = answer
    answer += "0" +  copy[::-1]
    return answer

solution([1, 7, 1, 2])

#참고풀이
def solution2(food):
    answer = ''
    for f in range(1, len(food)):
        answer += str(f) * (food[f]//2)
    return answer + "0" + answer[::-1]

solution2([1, 3, 4, 6])
