'''
* : 전 점수와 해당 점수를 두배로 만듬
# : 해당 점수가 마이너스 
'''
from curses.ascii import isalpha, isdigit

def solution(dartResult):
    result = []
    for idx, dart in enumerate(dartResult):
        if isalpha(dart):
            #숫자가 2자리일 때 실패함 ..
            int_dart = int(dartResult[idx-1])
            if int_dart == 0 and dartResult[idx-2] == "1":
                int_dart = 10
                
            if dart == "S":
                result.append(int(int_dart))
            if dart == "D":
                result.append(pow(int_dart, 2))
            if dart == "T":
                result.append(pow(int_dart, 3))
        elif dart == "*":
            result[-1] *= 2
            if idx <= 2:
                continue
            result[-2] *= 2
        elif dart == "#":
            result[-1] *= -1

    return sum(result)

# 참고 다른 풀이
def solution2(dartResult):
    scores = []
    dart = {'S': 1, 'D':2, 'T':3 }
    n = 0

    for idx, value in enumerate(dartResult):
        if value in dart:
            print(dartResult[n:idx])
            scores.append(int(dartResult[n:idx])**dart[value])
        if value == "*":
            #처음부터 -2까지 
            scores[-2:] = [x*2 for x in scores[-2:]]
        if value == "#":
            scores[-1] = -1 * scores[-1]
        if not isdigit(value):
            n = idx + 1

    return sum(scores)

solution2("1D2S#10S")
# solution("1S2D*3T")
# solution("1D#2S*3S")
# solution("1S*2T*3S")
# solution("1D2S3T*")
# solution("1D2S0T")