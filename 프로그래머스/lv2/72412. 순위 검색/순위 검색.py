from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(infomation, queries):
    info_dic = defaultdict(list)
    for info in infomation:
        info = info.split()
        condition = info[:-1]
        score = int(info[-1])
        for i in range(5): #-를 넣는 경우를 계산하는 거군..
            case = list(combinations([0,1,2,3],i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                info_dic[key].append(score)
    #점수 오름차순
    for value in info_dic.values():
        value.sort()
    result = []
    for query in queries:
        query = query.replace(" and ", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in info_dic:
            target_list = info_dic[target_key]
            idx = bisect_left(target_list, target_score)
            # print(target_list, target_score, idx)
            count = len(target_list) - idx
        result.append(count)
    # print(result)

    return result