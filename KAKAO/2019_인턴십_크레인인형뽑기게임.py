
from collections import deque

def solution(board, moves):
    new_board = list(map(deque, zip(*board))) #가로 -> 세로 변경

    for i in new_board:
        if 0 in i:
            while 0 in i:
                i.remove(0)
    result_list = []
    answer = []
    print(new_board)
    for item in moves:
        #print(new_board[item-1])
        if new_board[item-1]: #들어있으면, 비어있지 않으면
            #넣기 전에 비교 ,,
            pop_value = new_board[item-1].popleft()
            if result_list[-1] == pop_value:
                while result_list[-1] == pop_value:
                    new_board[item-1].popleft()
                    answer.append(pop_value)
            else:
                result_list.append(pop_value)
            
    return answer
        
    
    

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))