# https://school.programmers.co.kr/learn/courses/30/lessons/76502

# 내풀이
from collections import deque
from copy import deepcopy

def solution(s):
    if not s:
        return 0
    correct_dic = {'(': ')', '[': ']', '{': '}'}
    dq_s = deque(s)
    
    def check(dq_s):
        arr = []
        dq = deepcopy(dq_s)
        left_count, right_count = 0, 0
        while dq:
            val = dq.popleft()
            if val in correct_dic.keys():
                arr.append(val)
                left_count += 1
            else:
                right_count += 1
                if not arr or correct_dic[arr.pop()] != val: 
                    return False #오른쪽 괄호가 처음에 나오면 false
        return True if left_count == right_count else False

    def check_참고(s):
        st = []
        for e in s:
            if not st:
                st.append(e) #비어있으면 값 넣고
                continue
            #st[-1]이 왼쪽 괄호이고 e가 그에 맞는 짝인 오른쪽 괄호일때 
            if st[-1] in correct_dic and correct_dic[st[-1]] == e:
                st.pop()
            else: #짝이 안맞으면 넣음 
                st.append(e)
        return not st #짝이 맞는다면 st가 비어잇고 아니면 있을 것이므로 
    count = 0
    for _ in range(len(s)):
        if check_참고(dq_s):
            count += 1
        dq_s.append(dq_s.popleft()) # 처음부터 덱 수정하는 것이 아닌 계산하고 변경

    return count

print(solution("[](){}"))
# print(solution("()("))
# print(solution("{{{{{{"))
