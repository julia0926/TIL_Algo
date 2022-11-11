def solution(numbers, hand):
    left_loc = 10
    right_loc = 12
    using_hand = ""

    for val in numbers:
        if val in [1,4,7]: 
            left_loc = val
            using_hand += 'L'
        elif val in [3,6,9]:
            right_loc = val
            using_hand += ('R')
        elif val in [2,5,8,0]:
            if val == 0:
                val = 11 #0 = 11
            ldis = abs(val-left_loc)
            rdis = abs(val-right_loc)
            #오른쪽이 가깝다면 
            if ldis // 3 + ldis % 3 > rdis // 3 + rdis % 3:
                right_loc = val
                using_hand += ('R')
            #왼쪽이 가깝다면 
            elif ldis // 3 + ldis % 3 < rdis // 3 + rdis % 3: 
                left_loc = val
                using_hand += ('L') 
            #거리가 같다면 
            elif ldis // 3 + ldis % 3 == rdis // 3 + rdis % 3: 
                if hand == 'left':
                    left_loc = val
                    using_hand += ('L')
                else:
                    right_loc = val
                    using_hand += ('R')

    return using_hand

result = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	,"left")
print(result)