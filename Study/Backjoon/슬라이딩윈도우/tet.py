def solution(quiz):
    result = []
    for q in quiz:
        op = q.split('=')
        piv = eval(op[0].replace(' ', ''))
        if piv == int(op[1]):
            result.append("O")
        else:
            result.append("X")
    return result

solution(["3 - 4 = -3", "5 + 6 = 11"])