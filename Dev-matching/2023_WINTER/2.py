def solution(n, student, point):
    answer = 0
    arr = [[id, 0] for id in range(1, n+1)]
    for id, p in zip(student, point):
        #인덱스 찾음
        idx_tmp = 0
        for i in range(len(arr)):
            if arr[i][0] == id:
                arr[i][1] += p
                idx_tmp = i
        #정렬
        arr.sort(key=lambda x: (-x[1], x[0]))
        #0~2 -> 3~5
        #3~5 -> 0~2
        for i in range(n):
            if id == arr[i][0]:
                if idx_tmp in range(n//2) and i in range(n//2, n+1):
                    answer += 1
                elif idx_tmp in range(n//2, n+1) and i in range(n//2):
                    answer += 1
                    
    print(answer)
    return answer

solution(6, [6,1,4,2,5,1,3,3,1,6,5], [3,2,5,3,4,2,4,2,3,2,2])
solution(10, [3,2,10,2,8,3,9,6,1,2], [3,2,2,5,4,1,2,1,3,3])