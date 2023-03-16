
def solution(numbers):
    num_to_str = list(map(str,numbers))
    # 첫번째 자리 큰거 -> 문자열 길이 긴 것부터
    result = sorted(num_to_str,key=lambda x: x*3,reverse=True)
    # for i in num_to_str:
    #     print(i*3)
    # 문자열 기준 333 > 303030 더 크다
    answer = ''.join(result)
    return answer
print(solution([3, 30, 34, 5, 9]))

# arr = [333, 332030, 34, 5, 9]
# arr = list(map(str,arr))
# arr = sorted(arr,reverse=True)
# print(arr)
