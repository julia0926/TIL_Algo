
def solution(chicken):
    answer = 0
    while chicken >= 10:
        answer += chicken // 10
        chicken = chicken // 10 + chicken % 10
        print(answer, chicken)
    
    return answer

# print(solution(1081))
# print(solution(100))
print(solution(1999)) #222