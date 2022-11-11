from collections import deque
def solution(priorities, location):
    prlist = [i for i in range(len(priorities))]
    finish = [] 

    while len(priorities)!= 0:
        if priorities[0] == max(priorities):
            finish.append(prlist.pop(0)) 
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0)) #맨 앞 값을 맨뒤로
            prlist.append(prlist.pop(0)) #인덱스도 뒤로
        print(finish)
    return finish.index(location) +1 #값 리턴 
print(solution([1,2,8,3,4], 4))

# 1차시 실패 -> 문제 잘못 이해
# def solution(priorities, location):
#     list = priorities
#     piv = list[0]
#     for i in range(1, len(list)):
#         if piv >= list[i]: #기준보다 큰 값이 있다면
#             top = list.pop()
#             list.append(top)
#             piv = list[0]
#             if location == 0:
#                 location = len(list)-1
#             else:
#                 location -= 1
#         else: #기준이 제일 큰 값이라면 
#             return location

