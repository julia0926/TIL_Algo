# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    zero = 0
    common = 0
    for val in lottos:
        if val in win_nums:
            common += 1
        if val == 0:
            zero += 1
    if zero == 6:
        return [1, 6]
    elif common == 6:
        return [1, 1]
    elif zero == 0 and common == 0:
        return [6, 6]
    else:
        answer.append(7-(common+zero))
        answer.append(7-common)
        return answer

def solution_using_set(lottos, win_nums):
    common = len(set(win_nums).intersection(set(lottos)))
    zero = lottos.count(0)
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[common+zero], rank[common]]
    
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))