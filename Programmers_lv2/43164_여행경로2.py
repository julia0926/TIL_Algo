# https://school.programmers.co.kr/learn/courses/30/lessons/43164
from collections import defaultdict, deque

def solution(tickets):
    path = defaultdict(list)
    for a, b in tickets:
        path[a].append(b)
    
    for p in path.keys():
        path[p].sort() #value 값 알파벳 순으로 정렬 
    print(path)
    result = []
    dq = deque()
    dq.append("ICN")
    idx = 0
    while dq:
        idx += 1
       
        piv = dq[-1]
        if path[piv]: #path의 values()가 있으면
            dq.append(path[piv].pop(0))
        else: #도시가 없다면 
            result.append(dq.popleft())  #주어진 항공권이 남아있는지 확인하기 위해 재탐색 과정인가 ?
            
            # print(dq)
        print(result[::-1])
    return result

# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	)
# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]])
#답 : ["ICN", "CCC", "DDD", "ICN", "AAA", "BBB", "AAA", "BBB"]

# solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]])
#답  : 

