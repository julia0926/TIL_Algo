def solution(citations):
    citations.sort() #0,1,3,5,6
    for i in range(len(citations)):
        if len(citations) - i <= citations[i]:
            print(len(citations) - i)
            break
    answer = 0
    return answer

solution([3,0,6,1,5]) #3
solution([10, 8, 5, 4, 3]) #4