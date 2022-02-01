def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    rank = [0, 0, 0] #1번, 2번, 3번

    for i in range(len(answers)):
        if one[i % 5] == answers[i]:
            rank[0] += 1
        if two[i % 8] == answers[i]:
            rank[1] += 1
        if three[i % 10] == answers[i]:
            rank[2] += 1
    #print(max(rank))
    for i, v in enumerate(rank):
        if v == max(rank):
            answer.append(i + 1)
    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
