from collections import defaultdict, deque


def solution(tickets):
    travle_path = defaultdict(list)
    for go, end in tickets:
        travle_path[go].append(end)
    for k in travle_path.keys():
        travle_path[k].sort()
    
    result = []
    dq = deque()
    dq.append('ICN')
    
    while dq: 
        piv = dq[-1]
        print(piv)
        if not travle_path[piv]:
            result.append(dq.popleft())
            print("if", result)
        else:
            dq.append(travle_path[piv].pop())
            print("else:", dq)

    return result

#{'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']})

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])