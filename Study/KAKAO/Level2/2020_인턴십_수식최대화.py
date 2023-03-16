from collections import deque
from itertools import permutations
import re

def split_ex(expression):
    op_list = re.split('[0-9]+', expression)[1:]
    val_list = re.split('[*+-]', expression)
    piv_list = []
    for i in range(len(val_list)):
        piv_list.append(val_list[i]) 
        piv_list.append(op_list[i])
    
    return deque(piv_list[:-1])

def make_result(priority, expression):
    arr = split_ex(expression)
    for op in priority:
        tmp_list = []
        while arr:
            tmp = arr.popleft()
            if tmp == op: #연산자이면서 기준연산자랑 같으면
                result = str(eval(tmp_list.pop()+op+arr.popleft())) #연산자의 왼쪽값과 남아있는 배열의 값을 연산
                tmp_list.append(result) #마지막에 연산한 값을 추가
            else:
                tmp_list.append(tmp) #꺼낸값 그대로 넣음
        arr = deque(tmp_list)
    return int(arr.pop())

def solution(expression):
    permut_op = list(permutations("+-*", 3))
    answer = 0
    for op in permut_op:
        answer = max(answer, abs(make_result(op, expression)))
    return answer

print(solution("100-200*300-500+20"))