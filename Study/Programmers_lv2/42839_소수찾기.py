from itertools import permutations
import math


def getSosu(number):
    k = int(math.sqrt(number))
    if number < 2:
        return False
    for i in range(2, k+1):
        if number % i == 0:
            return False
        return True

def solution(numbers):
    result = []
    for i in range(1, len(numbers)+1):
        for i in list(map(''.join, permutations(numbers,i))):
            if getSosu(int(i)):
                result.append(int(i))

    print(len(set(result)))

solution("17")
solution("011")