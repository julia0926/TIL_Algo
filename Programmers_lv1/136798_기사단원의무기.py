#https://school.programmers.co.kr/learn/courses/30/lessons/136798
'''
number : 기사 단원의 수
limit : 공격력 제한수치
power : 제한수치 초과 공격력

result : 무기를 위한 철의 무게
'''

def all_divider(value):
    answer = []
    for i in range(1, value+1):
        answer.append(get_divider(i))
    return answer

def get_divider(value):
    answer = []
    for i in range(1, int(value**(1/2))+1):
        if value % i == 0:
            answer.append(i)
            print(answer, int(value**(1/2))+1)
            if i ** 2 != value:
                answer.append(value//i)
                print("제곱" ,answer, value, i ** 2)
    # print(answer)
    return len(answer)
    

def solution(number, limit, power):
    result = 0
    for i in all_divider(number):
        if i > limit: result += power
        else: result += i
    return result

    
    

get_divider(25)


# solution(5,3,2)
# print(solution(10,3,2))