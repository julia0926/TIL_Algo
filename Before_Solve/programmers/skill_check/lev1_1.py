def solution(s, n):
    answer = ''
    s = list(s)
    #print(s)
    for val in s:
        if val != ' ': #공백이 아니고
            val = ord(val) #아스키코드로 변환 
            
            
        else:
            answer += val
    return answer

print(solution("a B z", 4))