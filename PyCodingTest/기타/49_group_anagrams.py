#https://leetcode.com/problems/group-anagrams/

#그룹 애너그램 
from collections import defaultdict
def solution(arr):
    answer = defaultdict(list) #정렬해도 같은 값일 리스트를 넣기위함 
    for a in arr:
        answer[''.join(sorted(a))].append(a) #정렬한 문자열을 key값으로 디폴트딕리스트에 값 넣음 
    print(list(answer.values()))


solution(["eat","tea","tan","ate","nat","bat"])