
def dfs(depth, value,numbers,target):
    global answer
    if depth == len(numbers) and target == value:
        answer += 1
        return
    if depth == len(numbers):
        return
    dfs(depth+1, value+numbers[depth], numbers, target)
    dfs(depth+1, value-numbers[depth], numbers, target)

answer = 0

def solution(numbers, target):
    global answer
    dfs(0,0,numbers,target)
    return answer


print(solution([1, 1, 1, 1, 1], 3))