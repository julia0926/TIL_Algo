#https://leetcode.com/problems/daily-temperatures/

def dailyTemperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []
    for idx, now in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < now: #stack에 있는 인덱스값을 temp에서 찾아서 값을 비교
            i = stack.pop()
            result[i] = idx - i #pop한 위치에 온도차를 두어야함.
        stack.append(idx)
    return result
        

print(dailyTemperatures([73,74,75,71,69,72,76,73]))