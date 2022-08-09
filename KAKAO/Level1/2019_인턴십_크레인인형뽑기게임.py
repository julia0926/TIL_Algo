#https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    bucket = []
    answer = 0

    for i in moves: #행
        for j in range(len(board)): #열
            #행열 바꿔서 접근 
            if board[j][i-1] != 0: 
                bucket.append(board[j][i-1]) #바구니에 값 집어넣음
                board[j][i-1] = 0 #버켓에 집어넣었으니 0 처리
                # 바구니에 값이 2개 이상 있고, 끝에 2개가 같으면 
                if len(bucket) > 1 and bucket[-2] == bucket[-1]:
                    bucket.pop(-1)
                    bucket.pop(-1)
                    answer += 2
                break
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))