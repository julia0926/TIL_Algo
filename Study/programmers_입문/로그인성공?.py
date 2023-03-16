#https://school.programmers.co.kr/learn/courses/30/lessons/120883

def solution(id_pw, db):
    if id_pw in db:
        return "login"
    for id, pw in db:
        if id == id_pw[0]:
            return "wrong pw"
    return "fail"

   

print(solution(["meosseugi", "1234"], 
[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))