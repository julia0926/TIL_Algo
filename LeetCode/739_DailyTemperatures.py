def dailyTemperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)
    for idx, val in enumerate(temperatures):
        while stack and val > temperatures[stack[-1]]: #현재값이 스택의 마지막 값보다 크다면
            last = stack.pop() #스택의 최근값 pop
             #현재 인덱스(온도 높은) - 비교 대상 -> 차이는 기다린 정도
            result[last] = idx - last
        stack.append(idx) 
    return result

print(dailyTemperatures([73,74,75,71,69,72,76,73]))