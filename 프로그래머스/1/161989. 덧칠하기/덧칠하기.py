def solution(n, m, section):
    answer = 0
    current = 0
    for sec in section:
        
        # print(current)
        if current <= sec:
            current = sec + m
            answer += 1
    print(answer)
    return answer