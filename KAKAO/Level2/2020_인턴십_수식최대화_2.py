from collections import deque
from itertools import permutations
import re

def split_expression(expression):
    num_arr = re.split('[-+*]', expression)
    op_arr = re.split('[0-9]+', expression)[1:]
    arr = []
    for a, b in zip(num_arr, op_arr):
        arr.append(a)
        arr.append(b)
    return deque(arr[:-1])

def solution(expression):
    oper = list(permutations(['+','-','*'], 3))
    # print(oper)
    def make_result(operation):
        dq = split_expression(expression) 
        for op in operation:
            arr = []
            while dq:
                val = dq.popleft()
                if op == val:
                    arr.append(eval(str(arr.pop())+op+str(dq.popleft())))
                else:
                    arr.append(val)
            dq = deque(arr)
        return abs(int(arr[0]))
    result = []
    for op in oper:
        result.append(make_result(op))
    return max(result)

solution("100-200*300-500+20")