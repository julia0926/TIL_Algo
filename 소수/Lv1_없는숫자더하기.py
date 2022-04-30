# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    #내코드
    arr = [0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        if i in arr:
            arr.remove(i)
    return sum(arr)
    #참고) set 나도 생각했는데 ...
    # return sum(set(range(10)) - set(numbers))

print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))