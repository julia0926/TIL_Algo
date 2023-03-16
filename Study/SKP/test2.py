'''
1조직 = 1보스
수익금 보낼 보스 없으면 그사람 = 해당최종보스
!!! 해당조직의 조직원수 구하기(최종보스포함)
q = 보스
b = 조직원
조직원이 최종보스인 경우 = 조직원수구함(최종보스포함)
-1 최종보스 = 조직의 개수 
'''

# def solution(p, b):
#     #p[i]=-1인지 확인 보스인지 확인 아니면 조직원수 0
#     result = []
#     for id in b:
#         if p[id] != -1: #최종보스가 아니라면 
#             result.append(0)
#         member_count = 0
#         boss = {} #보스: 조직원들
#         for index, employee in enumerate(p):
#             if employee == id:
#                 member_count += 1 #구성원이라면 
#             #i가 조직원 p[i]가 보스
#             if p[index] != -1:
#                 boss[p[index]] = index
#             print(boss)

#     answer = []
#     return answer


def solution(p, b):
    children = [[] for _ in range(len(p))]
    for i in range(len(p)):
        parent = p[i]
        if parent == -1:
            continue
        children[parent].append(i)

    def dfs(node):
        result = 1
        for v in children[node]:
            result += dfs(v)
        return result
    
    answer = []
    for i in range(len(b)):
        member = b[i]
        if p[member] != -1:
            answer.append(0)
        else:
            answer.append(dfs(member))
    return answer

solution([2, 2, -1, 1, 5, -1, 5], [2, 5])
solution([2, 2, -1, 1, 5, -1, 5], [1, 5])