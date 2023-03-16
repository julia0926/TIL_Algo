#문제 : https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations, count
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        combi_list = []
        for order in orders:
            
            combi_list += list(combinations(sorted(order), c)) #<<- ✅여기서 실수 함 !!!! sorted 안함
            
        counter_dic = Counter(combi_list).most_common() #dic -> arr
        for menu, count in counter_dic:
            print(menu, count)
            if counter_dic[0][1] == count and count > 1: #제일많이 주문된 횟수와 횟수가 1번이 넘으면 
                answer.append("".join(menu))
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))

'''
✅
왜 실수했냐 ? 
정렬을 하고 combination을 만들어야 제한사항에서 주어진 사전순으로 오름차순 정렬해서 return 함
print(order)
print("정렬", list(combinations(sorted(order), c)))
print("그냥", list(combinations(order, c)))
>> 출력
WXA
정렬 [('A', 'W'), ('A', 'X'), ('W', 'X')]
그냥 [('W', 'X'), ('W', 'A'), ('X', 'A')]
'''