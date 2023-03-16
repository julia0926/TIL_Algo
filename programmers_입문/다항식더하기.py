import re
def solution(polynomial):
    v_number = 0
    number = 0
    if 'x' not in polynomial:
        return polynomial
    else:
        for v in polynomial.split(" + "):
            if v[-1] == 'x':
                if len(v) == 2:
                    v_number += int(v[0])
                else:
                    v_number += 1
            else:
                number = int(v)
        if number != 0:
            answer = f'{v_number}x + {number}'
        else:
            if v_number != 1:
                answer = f'{v_number}x'
            else:
                answer = 'x'
        return answer
print(solution("3x + 7 + x"))
print(solution("0"))