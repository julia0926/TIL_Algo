def solution(numbers):
    answer = []

    for n in numbers:
        bit = bin(n)
        min_v = 1e9
        i = 0
        while True:
            i += 1
            #최소 값이 바뀌면 
            xor = bin(n ^ (n+i))
            if str(xor[2:]).count('1') <= 2:
                break
            min_v = min(str(xor[2:]).count('1'), min_v)
        answer.append(n+i)

    return answer

print(solution([2,7]))

#https://school.programmers.co.kr/questions/30178 해결하기 !! 시간초과