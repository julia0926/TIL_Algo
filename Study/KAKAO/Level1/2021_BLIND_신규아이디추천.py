import re

def solution(new_id):
    st = new_id.lower() #1
    st = re.sub('[^a-z0-9\-_.]', '' ,st) #2
    st = re.sub('\.+', '.', st) #3
    st = re.sub('^[.]|[.]$', '', st) #4
    #5
    if len(st) == 0:
        st = "a"
    #6
    if len(st) >= 16:
        st = st[:15]
        if st[-1] == '.':
            st = st[:-1] #마지막 문자를 제거해서 보임 
    #7
    if len(st) <= 2:
        while len(st) < 3:
            st += st[-1]
    
    return st

solution("...!@BaT#*..y.abcdefghijklm")