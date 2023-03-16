from collections import defaultdict

def solution(s):
    freq = defaultdict(list)
    answer = []
    for idx, alpha in enumerate(s):
        if alpha not in freq:
            freq[alpha].append(idx)
            answer.append(-1)
        else:
            answer.append(idx - freq[alpha][-1])
            freq[alpha].append(idx)
    return answer
 
solution("banana")
            
            
            