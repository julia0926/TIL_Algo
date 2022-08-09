def balance(str):
    left_count, right_count = 0, 0
    for idx, value in enumerate(str):
        if value == "(": left_count += 1
        else: right_count += 1
        if left_count == right_count:
            return str[:idx+1], str[idx+1:]

def correct(str):
    #문자열의 괄호의 짝이 맞을 때 올바른 문자열 
    tmp_list = []
    for s in str:
        if s == "(":
            tmp_list.append(s)
        else:
            if not tmp_list: #비어있으면 
                return False
            else:
                tmp_list.pop()
    return True


def solution(p):
    if not p:
        return ""
    u, v = balance(p)
    correct_result = correct(u)
    if correct_result:
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        for value in u[1:len(u)-1]:
            if value == "(":
                answer += ")"
            else: answer += "("
            
    return answer

print(solution("()))((()") == "()(())()")