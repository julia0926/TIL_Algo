def solution(a, b):
    answer = 0
    for x, y in zip(a, b):
        answer += (x*y)
    return answer
    # 한줄로 파이썬 답게 하면 
    # return sum([(x*y) for x, y in zip(a, b)])

print(solution([1,2,3,4], [-3,-1,0,2]))