def balance(w):
    left_count, right_count = 0, 0
    for idx, value in enumerate(list(w)):
        if value == "(":
            left_count += 1
        else:
            right_count += 1

        if left_count == right_count:
            return w[:idx+1], w[idx+1:]

def correct(u):
    temp = []
    for i in list(u):
        if i == "(":
            temp.append("(")
        else:
            if not temp:
                return False
            temp.pop()
    return True


def solution(p):
    if not p:
        return ""
    u, v = balance(p)
    if correct(u): return u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        for i in u[1:len(u)-1]:
            if i == "(": answer += ")"
            else: answer += "("
        return answer
    