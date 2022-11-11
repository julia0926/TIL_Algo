# https://school.programmers.co.kr/learn/courses/30/lessons/76502

# 내풀이
from collections import deque
from copy import deepcopy

def solution(s):
    if not s:
        return 0
    correct_dic = {'(': ')', '[': ']', '{': '}'}
    dq_s = deque(s)

    def check(dq_s):
        arr = []
        dq = deepcopy(dq_s)
        left_count, right_count = 0, 0
        while dq:
            print(arr)
            val = dq.popleft()
            # print(dq, val)
            if val in correct_dic.keys():
                arr.append(val)
                left_count += 1
            else:
                right_count += 1
                if not arr or correct_dic[arr.pop()] != val: 
                    return False #오른쪽 괄호가 처음에 나오면 false
        return True if left_count == right_count else False

    count = 0
    for i in range(len(s)):
        if i != 0:
            dq_s.append(dq_s.popleft())
        if check(dq_s):
            count += 1
    return count

# print(solution("[](){}"))
# print(solution("()("))
print(solution("{{{{{{"))

