#https://school.programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    student = [i for i in range(1, n+1)]
    #제한사항 구하기 위함 
    not_borrow = list(set(lost) & set(reserve)) 
    if not_borrow:
        for n in not_borrow:
            lost.remove(n)
            reserve.remove(n)
    for r in sorted(reserve):
        if r - 1 in lost:
            lost.remove(r-1)
        elif r + 1 in lost:
            lost.remove(r+1)

    return len(set(student) - set(lost))

# solution(7,[7],[1,3,5]) # 5
# solution(5,[2,4], [1,3,5])
print(solution(5,[4,2],[3,5] ))