# 참고해서 푼 문제 !!!!

from itertools import permutations
import math
def check(n): #소수 구하는 메소드
    k = math.sqrt(n) # 제곱수는 소수가 아니므로 
    if n < 2:
        return False
    for i in range(2, int(k)+1):
        if n % i == 0: #자기보다 작은 값 중 나눠지는 값이 있으면 소수아님
            return False 
        return True

def solution(numbers):
    result = []
    for k in range(1, len(numbers)+1): #k길이만큼 조합 경우의 수가 생김
        # permutations([1,2,3],2)
        # [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]
        perlist = list(map(''.join, permutations(list(numbers),k)))  #nPr
        # print(perlist)
        for i in list(set(perlist)): #set은 중복을 허용 X
            if check(int(i)):
                result.append(int(i))
    answer = len(set(result))
    return answer

solution("011")

# 1. 나올 수 있는 경우의 수 다 구해서
# 2. 그 중 소수 구하기 

