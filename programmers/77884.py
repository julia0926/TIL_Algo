# 약수의 개수와 덧셈 : https://programmers.co.kr/learn/courses/30/lessons/77884
def calculate(value):
    divisors = []
    for i in range(1, value+1):
        if (value % i) == 0:
            divisors.append(i)
    return len(divisors)

def solution(left, right):
    answer = 0
    for v in range(left, right+1):
        num = calculate(v) #약수의 개수를 구함 
        if num % 2 == 0: #약수의 개수가 짝수라면 ?
            answer += v
        else:
            answer -= v
    return answer

print(solution(13, 17))
print(solution(24, 27))

