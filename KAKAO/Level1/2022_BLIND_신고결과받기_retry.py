#https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    #1. id별로 신고한 딕셔너리 생성
    report_dic = {id: [] for id in id_list} #{신고 당한사람: 신고한 사람}
    answer = [0 for _ in range(len(id_list))] 
    #2. 유저가 신고한 id 리스트 넣기
    for value in set(report): #동일한 신고건 안됨
        reporter, reported = value.split()
        report_dic[reported].append(reporter)
    #3. 정지된 ID 찾기
    for key, value in report_dic.items():
        if len(value) >= k: #k번 이상 신고 받았으면
            #print(key) #정지된 유저 id
            for i in value: #key를 신고한 유저 리스트 value 들에게
                answer[id_list.index(i)] += 1 #정지 메일 발송 +1
    return answer

#결과 : 유저별로 처리 결과 메일을 받은 횟수       
print(solution(["muzi", "frodo", "apeach", "neo"], 
["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
