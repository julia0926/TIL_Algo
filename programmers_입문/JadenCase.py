def solution(s):
    answer = s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == ' ' and s[i] != ' ': #이전 항목이 공백이고, 지금이 알파벳이라면
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer

            
solution("3  peop  le    unF  ollowed me")