
def solution(N):
    #양쪽의 0을 버림~
    return len(max(format(N, 'b').strip('0').split('1'), key=len))
    # print(val, val.strip('0'))
    # arr = val.split('1')
    

# print(solution(20))
print(solution(1041)) #5
print(solution(51712))