def solution(numbers, hand):
    answer = ""
    left_loc, right_loc = 10, 12
    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            left_loc = number
        elif number in [3, 6, 9]:
            answer += "R"
            right_loc = number
        else:
            if number == 0:
                number = 11 #0은 11번째로 처리 
            left_dist = abs(number - left_loc)
            right_dist = abs(number - right_loc)
            if left_dist // 3 + left_dist % 3 > right_dist // 3 + right_dist % 3: #왼쪽이 더 가까우면 
                answer += "R"
                right_loc = number
            elif left_dist // 3 + left_dist % 3 < right_dist // 3 + right_dist % 3:
                answer += "L"
                left_loc = number
            elif left_dist // 3 + left_dist % 3 == right_dist // 3 + right_dist % 3:
                if hand == "left":
                    answer += "L"
                    left_loc = number
                else:
                    answer += "R"
                    right_loc = number
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL")
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")