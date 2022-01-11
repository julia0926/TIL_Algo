# info : 지원자의 정보
# query : 개발 팀이 궁금해하는 문의조건 

from re import split

def solution(info, query):
    answer = []
    for k in range(len(info)):
        info[k] = info[k].split()
    for c in range(len(query)): #query 배열 하나씩 
        data = query[c].split('and') #한 줄의 배열을 and 기준으로 자름
        #print(data2)
        for i in range(len(data)):
            data[i] = data[i].strip() #양쪽 공백을 없앰
            if i == 3:
                last = data[i].split()
                data.pop()
                data.append(last[0])
                data.append(last[1])
        query[c] = data

    for case in query:
        count = 0
       
        for human in info:
            if case[0] != human[0] and case[0] != '-':
                continue
            if case[1] != human[1] and case[1] != '-':
                continue
            if case[2] != human[2] and case[2] != '-':
                continue
            if case[3] != human[3] and case[3] != '-':
                continue
            if int(human[4]) >= int(case[4]):
                count+=1
                    
        answer.append(count)
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))