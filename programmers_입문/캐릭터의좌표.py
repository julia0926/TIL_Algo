def solution(keyinput, board):
    max_row, max_col = board[0]//2, board[1]//2
    now = [0, 0]
    for key in keyinput:
        # print(now)
        if key == "left" and now[0] > -max_row:
            now[0] -= 1
        elif key == "right" and now[0] < max_row:
            now[0] += 1
        elif key == "up" and now[1] < max_col: 
            now[1] += 1
        elif key == "down" and now[1] > -max_col:
            now[1] -= 1
    return now

print(solution(["left", "right", "up", "right", "right"], [11,11]))
print(solution(["down", "down", "down", "down", "down"], [7,9]))