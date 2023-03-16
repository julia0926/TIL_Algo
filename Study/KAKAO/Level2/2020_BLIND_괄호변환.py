# 균형잡힌 = 괄호 개수가 같으면 
# 올바른 괄호문자열 = 괄호 짝이 맞으면 

#균형잡힌 문자열 
def divide(p):
    left_cnt, right_cnt = 0, 0
    for idx, value in enumerate(p):
        if value == "(": left_cnt += 1
        else: right_cnt += 1
        if left_cnt == right_cnt:
            return p[:idx+1], p[idx+1:]

#올바른 괄호 문자열인지
def check(u):
    tmp_list = []
    for p in u:
        if p == '(':
            tmp_list.append(p)
        else: #p == )
            if not tmp_list:
                return False
            else: tmp_list.pop()
    return True

def solution(p):
    if not p: #1
        return ""
    #2 균형잡힌 , 문자열 
    u, v = divide(p)
    if check(u):
        return u + solution(v)
    else:
        answer = "".join('(')
        answer += solution(v)
        answer += ')'
        for k in u[1:len(u)-1]:
            if k == '(':
                answer += ')'
            else:
                answer += '('

    return answer
    
print(solution(")("))
print(solution("()))((()"))