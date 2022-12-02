#https://school.programmers.co.kr/learn/courses/30/lessons/140108#
from collections import defaultdict 

#1차시도 -> 28.6
def solution_(s):
    dic = defaultdict(int)
    answer = 0
    for ch in s:
        dic[ch] += 1
        dic_len = len(dic.values())
        if dic_len > 1 and dic_len != len(set(dic.values())):
            answer += 1
            # print(dic)
            dic = defaultdict(int)
    if dic:
        answer += 1
    return answer

# solution("aaabbaccccabba")
solution("abracadabra")
