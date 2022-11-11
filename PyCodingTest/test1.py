from itertools import permutations

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    return True

def solution(numbers):
    #흩어진 조각 모음 종류
    answer = 0
    arr = list(numbers)
    combi = []
    result = set()
    for i in range(1, len(numbers)+1):
        combi.extend(list(permutations(arr, i)))
        for i in combi:
            result.add(int(''.join(i)))
    for i in result:
        if is_prime(i):
            answer += 1
    #소수인지 판별 
    return answer
    

print(solution("17"))
print(solution("011"))


'''
#####1차 시도 : 정확성 33%
from itertools import permutations


def solution(numbers):
    #흩어진 조각 모음 종류
    arr = list(numbers)
    combi = []
    for i in range(1, len(numbers)+1):
        k = list(permutations(arr, i))
        for i in k:
            word = ''.join(i)
            if word not in combi and word[0] != '0': #중복 제거 
                combi.append(''.join(i))
    #소수인지 판별 
    max_val = int(combi[-1])
    prime = [False, False] + [True] * (max_val - 1)
    for i in range(2, max_val+1):
        if prime[i]:
            for j in range(i*2, max_val+1, i):
                prime[j] = False #소수 아님 
    cnt = 0
    for i in combi:
        if prime[int(i)]:
            cnt += 1
    return cnt
'''