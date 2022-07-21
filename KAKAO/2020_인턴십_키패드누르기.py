

def get_distance(now_loc, next_loc):
    pad = {1: [0, 0], 2: [1, 0], 3: [2, 0],
              4: [0, 1], 5: [1, 1], 6: [2, 1],
              7: [0, 2], 8: [1, 2], 9: [2, 2],
              "*": [0, 3], 0: [1, 3], "#": [2, 3], }

    x1, y1 = pad[now_loc]
    x2, y2 = pad[next_loc]
    return abs(x1-x2) + abs(y1-y2)

def solution(numbers, hand):
    #키패드 위치
    answer = ""
    left_loc, right_loc = "*", "#"
   
    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            left_loc = number
        elif number in [3, 6, 9]:
            answer += "R"
            right_loc = number
        else:
            left_dis = get_distance(left_loc, number) 
            right_dis = get_distance(right_loc, number) 
            if left_dis < right_dis: #왼쪽이 더 가깝다
                answer += "L"
                left_loc = number
            elif left_dis > right_dis: #오른쪽이 더 가깝다
                answer += "R"
                right_loc = number
            else:
                if hand == "left":
                    answer += "L"
                    left_loc = number
                else:
                    answer += "R"
                    right_loc = number
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL")
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")