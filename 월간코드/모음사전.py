#https://school.programmers.co.kr/learn/courses/30/lessons/84512
#참고 : https://jyeonnyang2.tistory.com/226
def dfs(x, tmp_list, alpha):
    print(tmp_list)
    tmp_list.append(x)
    for i in alpha:
        if len(x) != len(alpha):
            dfs(x+i, tmp_list, alpha)
        else:
            x[:-1]

def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    tmp_list = []
    for value in alpha:
        dfs(value, tmp_list, alpha)
    return tmp_list.index(word) + 1


print(solution("I"))