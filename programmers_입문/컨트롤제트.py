def solution(s):
    result = []
    for i in s.split():
        if i == 'Z':
            result.pop()
        else:
            result.append(int(i))
    return sum(result)

print(solution("1 2 Z 3"))
print(solution("10 Z 20 Z 1"))