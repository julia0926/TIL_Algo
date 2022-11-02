def solution(arr):
    arr.sort()
    sum = 0
    for i, n in enumerate(arr):
        if i % 2 == 0:
            sum += n
    return sum
    
def solution2(arr):
    return sum(sorted(arr)[::2])

solution([1,4,3,2])
print(solution2([1,4,3,2]))