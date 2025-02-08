def solution(ingredient):
    answer = 0
    stack = []
    for ing in ingredient:
        stack.append(ing)
    
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                stack.pop()
    return answer