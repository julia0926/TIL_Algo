from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        tmp = []
        for order in orders:
            combi = list(combinations(sorted(order), c))
            tmp += combi
        count_dic = Counter(tmp).most_common()

        for menu, cnt in count_dic:
            if cnt > 1 and cnt == count_dic[0][1]:
                answer.append("".join(menu))        
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]) == ["AC", "ACDE", "BCFG", "CDE"])