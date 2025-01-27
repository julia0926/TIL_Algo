def solution(t, p):
    slice_len = len(p)
    range_len = len(t)-slice_len+1
    result = 0
    for i in range(range_len):
        if t[i:i+slice_len] <= p:
            result += 1
    
    return result

solution("3141592", "271")