from itertools import permutations
from math import perm
import re

def calculate(v1, v2, op):
    v1, v2 = int(v1), int(v2)
    if op == "*":
        return str(v1 * v2)
    elif op == "+":
        return str(v1 + v2)
    else:
        return str(v1 - v2)

def change(op_list, expression):
    input_op = re.split('[0-9]+', expression)[1:]
    input_val = re.split('[-+*]', expression)
    new_op_list, new_val_list = [], []
    for op in op_list: #연산자 리스트 3개 중 하나씩 
        #입력된 연산자 리스트에 해당 연산자가 있을때까지
        print("기준 !! ", op, op_list)
        
        while len(input_op) == 0:
            print("비면 종료", len(input_op))
            piv_op = input_op.pop(0)
            print(piv_op, input_val, input_op)
            if piv_op == op: #같으면 그 값 두개뽑고 연산자 하나 뽑아서 계산
                v1 = input_val.pop(0)
                v2 = input_val.pop(0)
                new_val_list.append(calculate(v1, v2, piv_op))
                print("계산됨 !")
            else: #다르다면 연산자 값 pop
                new_val_list.append(input_val.pop(0))
                new_op_list.append(piv_op)
        new_val_list.append(input_val.pop(0))
        input_op = new_op_list
        input_val = new_val_list
    
    print("마지막", new_val_list)

def solution(expression):
    permut_op = list(permutations("+-*", 3))
    for op in permut_op:
        change(op, expression)

    answer = 0
    return answer

solution("100-200*300-500+20")