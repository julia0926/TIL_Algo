# 정렬 : K번째 수

def solution(array, commands):
    result = []
    for com in commands:
        i, j, k = com
        result.append(list(sorted(array[i-1:j]))[k-1])
    return result
solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])
# 1번째 풀이
# def solution(array, commands):
#     c = commands
#     l = []
#     for i in range(len(commands)):
#         start = c[i][0]-1
#         end = c[i][1]
#         th = c[i][2]-1
#         arr = sorted(array[start:end])
#         l.append(arr[th])
#     return l
# solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])