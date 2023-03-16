#https://school.programmers.co.kr/learn/courses/30/lessons/138476
def dynamic_programming(arr):
    cache = [None] * len(arr)
    # 1.
    cache[0] = arr[0]

    # 2.
    for i in range(1, len(arr)):
        cache[i] = max(0, cache[i-1]) + arr[i]
    print(cache)
    return max(cache)

dynamic_programming([1,2,3,4,1])