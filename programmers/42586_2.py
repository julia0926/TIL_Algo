def solution(progresses, speeds):
    answer = []
    while progresses:
        result = 0
        if progresses[0] < 100:
            for idx, speed in enumerate(speeds):
                progresses[idx] += speed
                print(idx)
        else:
            while progresses and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                result += 1
            answer.append(result)
    return answer

print(solution([93, 30, 55],[1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))