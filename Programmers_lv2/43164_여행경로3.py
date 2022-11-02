from collections import defaultdict


def solution(tickets):
    path = defaultdict(list)
    
    for a, b in tickets:
        path[a].append(b)
    

    answer = []
    return answer

solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]])
# 결과 : ["ICN", "CCC", "DDD", "ICN", "AAA", "BBB", "AAA", "BBB"]