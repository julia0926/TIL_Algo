def solution(n, times):
    times.sort()
    start, end = times[0], n * times[1]
    result = 0
    
    while start <= end:

        mid = (start + end) // 2
        count = 0
        for time in times:
            count += mid // time
            if count >= n: #<< 여기가 핵심이엿음!!!!
                break
        
        if n <= count: #더 시간이 초과되는건 ㄱㅊ은데 적으면 안됌
            end = mid - 1
            result = mid

        elif n > count: #더 작으면 
            start = mid + 1 


    return result
print(solution(6, [2,5]))