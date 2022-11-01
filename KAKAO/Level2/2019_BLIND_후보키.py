#https://school.programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations
def solution(relation):
    row = len(relation) #row명
    col = len(relation[0]) #몇개의 속성
    combi = []
    #속성의 조합을 만들어냄
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))

    #이제 계산 (조합별로 값 저장)

    unique = [] #유일성 조합
    for c in combi: 
        combi_list = [tuple(rel[key] for key in c) for rel in relation] #조합별 값들의 조합을 구함 
        if len(set(combi_list)) == row: #유일한가?
            put = True

            for x in unique:
                if set(x).issubset(set(c)): #유일한 조합이 지금의 조합의 자식조합이면 ? 
                    #ex) 학번이 유일한데, 학번을 포함한 다른 조합들은 최소성에 부합 X
                    print(x, c) # (0,) (0, 2)
                    put = False
                    break
            if put: unique.append(c)
    return len(unique)


solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])