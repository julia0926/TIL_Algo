#문제 : https://www.boostcourse.org/selfcheck/lecture/1410049/?isDesc=false

def solution(arr):
    set_arr = set(arr)
    counter_dic = {k: 0 for k in set_arr}

    for i in arr:
        counter_dic[i] += 1
    result = []
    for i in set_arr:
        if counter_dic[i] > 1:
            result.append(counter_dic[i])

    if not result:
        print([-1])
    else:
        print(result)

solution([1, 2, 3, 3, 3, 3, 4, 4])
solution( [3, 2, 4, 4, 2, 5, 2, 5, 5])
solution([3, 5, 7, 9, 1])