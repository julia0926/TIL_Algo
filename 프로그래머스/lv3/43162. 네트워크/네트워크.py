def solution(n, computers):
    temp = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]: #연결 됐다면, 1이라면
                for k in range(n):
                    if temp[k] == temp[i]: #이웃한 것끼리 연결되어있다면
                        print(temp[k] , temp[i],  temp[j])
                        temp[k] = temp[j] #이웃한 노드에도 연결상태를 부여한다.
    return len(set(temp))