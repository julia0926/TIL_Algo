def solution(mylist):
    answer = []
    for v in mylist:
        if v % 2 != 0:
            answer.append(pow(v, 2))
    return answer
    #위의 문장 한줄로 표현 
    return [pow(v, 2) for v in mylist if v % 2 != 0]

print(solution([3,2,6,7]))