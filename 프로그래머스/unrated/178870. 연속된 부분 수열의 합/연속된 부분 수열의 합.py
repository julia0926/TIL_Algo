def solution(sequence, k):
    n = len(sequence)
    #누적합
    # dp = [0] * n
    # dp[0] = sequence[0]
    # answer = []
    # for i in range(1, n):
    #     dp[i] = sequence[i] + dp[i-1]
    
    interval_sum = 0
    end = 0
    count = 0
    answer = []
    for start in range(n):
        while interval_sum < k and end < n:
            interval_sum += sequence[end]
            end += 1
        if interval_sum == k:
            answer.append([start, end-1])
        interval_sum -= sequence[start]
    
    diff = []
    for a in answer:
        diff.append(a[1] - a[0])
    
    idx = diff.index(min(diff))
    return answer[idx]