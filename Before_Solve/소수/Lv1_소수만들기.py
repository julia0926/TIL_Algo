# https://programmers.co.kr/learn/courses/30/lessons/12977

#소수 판별 함수 -> 에라토스 테네스의 체
def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    from itertools import combinations

    pick_value = list(combinations(nums, 3))
    answer = 0
    for value in pick_value:
        if is_prime(sum(value)):
            answer += 1
    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))