#https://school.programmers.co.kr/learn/courses/4008/lessons/72546
def solution(mylist):
    # 내풀이 
    #answer = []
    #second_list = [mylist[i] for i in range(1, len(mylist))]
    #for a, b in zip(mylist, second_list):
    #    answer.append(abs(a-b))
    #return answer
    # 참고 해답 : second_list를 만들지 않고 그냥 슬라이싱 가능
    answer = []
    for a, b in zip(mylist, mylist[1:]):
        answer.append(abs(a-b))
    return answer

print(solution([83, 48, 13, 4, 71, 11]))