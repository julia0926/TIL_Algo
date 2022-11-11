def solution(arr, divisor):
    answer = [v for v in arr if v % divisor == 0]
    # for v in arr:
    #     if v % divisor != 0:
    #         continue
    #     answer.append(v)
    answer.append(-1) if len(answer) == 0 else answer.sort()
    # if len(answer) == 0:
    #     answer.append(-1)
    # else:
    #     answer.sort()
    return answer

# 1차시도 
# def solution(arr, divisor):
#     answer = []
#     for v in arr:
#         if v % divisor != 0:
#             continue
#         answer.append(v)
#     if len(answer) == 0:
#         answer.append(-1)
#     else:
#         answer.sort()
#     return answer

print(solution([5, 9, 7, 10], 5))
