#https://programmers.co.kr/learn/courses/30/lessons/42888

# 나간 후  이름을 바꾸고 들어와도 기존 이름도 바뀜 
# 

def solution(record):
    answer = []
    userinfo = dict()
    logs = []

    for re in record:
        arr = re.split()
        state, userid = arr[0], arr[1]
        if len(arr) == 3: 
            userinfo[userid] = arr[2]
        logs.append((state,userid))
    for log in logs:
        state, userid = log[0], log[1]
        if state == "Enter":
            answer.append(f'{userinfo[userid]}님이 들어왔습니다.')
        elif state == "Leave":
            answer.append(f'{userinfo[userid]}님이 나갔습니다.')
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
