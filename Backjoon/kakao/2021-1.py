import re

def solution(new_id):
    new_id = new_id.lower() #1단계 
    new_id = re.sub('[^0-9a-z-_.]','',new_id) #2단계
    new_id = re.sub('\.+','.',new_id) #3단계
    # \ : 특수문자를 보통의 문자처럼 비교할 때 
    # + : 1개 이상 
    #4단계
    new_id = new_id.strip('.')
    #5단계
    if new_id == "":
        new_id = 'a'
    #6단계   
    if len(new_id) > 15:
        new_id = new_id[0:15]
        if new_id[-1] == '.':
            new_id = new_id.rstrip('.')
    #7단계
    if len(new_id) <= 2:
        c = new_id[-1]
        while len(new_id)!=3:
            new_id += c
    return new_id

print(solution("z-+.^."))