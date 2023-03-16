'''
균형잡힌 = 괄호 개수 같음
올바른 = 짝도 맞눈다
'''
from collections import deque
def devide(w):
    left, right = 0, 0
    dq = deque(w)
    for i in range(len(w)):
        value = dq.popleft()
        if value == '(':
            left += 1
        else:
            right += 1
        if left == right and left != 0:
            return w[:i+1], w[i+1:]

def correct(u):
    dq = deque(u)
    count = 0
    while dq:
        value = dq.popleft()
        if value == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True if count == 0 else False

def solution(p):
    if len(p) == 0:
        return p
    u, v = devide(p)
    if correct(u):
        return u + solution(v)
    else:
        answer = ''.join('(') + solution(v)
        answer += ')'
        for t in u[1:len(u)-1]:
            if t == '(':
                answer += ')'
            else:
                answer += '('
        return answer
    
# print(solution("(()())()"))
# print(solution(")("))
print(solution("()))((()"))