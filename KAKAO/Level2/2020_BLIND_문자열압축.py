def solution(s):
    answer = 1e9
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2+1): #1개부터 ~ 문자열길이//2
        result = ''
        cnt = 1
        first = s[:i] #첫번째 부분 
        for j in range(i, len(s)+i, i): #index 0~문자열 길이까지, slice 주기로
            if first == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1: #문자열이 한개 밖에 없다면 
                    result += first 
                else:
                    result += str(cnt) + first
                first = s[j:j+i]
                cnt = 1
        answer = min(answer, len(result)) #현재보다 더 길이가 짧은게 답 .. 
    return answer
print(solution("ababcdcdababcdcd"))