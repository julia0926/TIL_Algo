def solution(lines):
    answer = 0
    #두 선분 겹치는 부분
    for a, b in [(0,1), (1,2), (0,2)]:
        a_start, a_end = lines[a]
        b_start, b_end = lines[b]
        max_s = max(a_start, b_start)
        min_e = min(a_end, b_end)
        print(max_s, min_e)
        if min_e > max_s:
            answer += min_e - max_s
    #세 선분 겹치는 부분

    max_start, min_end = -100, 100
    for i in range(3):
        max_start = max(max_start, lines[i][0])
        min_end = min(min_end, lines[i][1])
    if min_end > max_start:
        answer -= (min_end-max_start) * 2

    return answer
