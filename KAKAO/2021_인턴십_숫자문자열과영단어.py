#https://school.programmers.co.kr/learn/courses/30/lessons/81301
#문자열 -> 숫자로 
def solution(s):
    alpha_dic = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    for key, value in alpha_dic.items():
        if value in s:
            s = s.replace(value, str(key))
    return int(s)

solution("23four5six7")