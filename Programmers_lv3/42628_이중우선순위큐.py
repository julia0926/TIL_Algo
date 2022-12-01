import heapq 

def solution(operations):
    answer = []
    for op in operations:
        if op[0] == 'I':
            heapq.heappush(answer, int(op[2:]))
        elif op[-2:] == '-1':
            if answer:
                heapq.heappop(answer)
        else:
            if answer:
                max_val = max(answer)
                answer.remove(max_val)
    if not answer:
        return [0, 0]
    
    return [max(answer), min(answer)]

solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])