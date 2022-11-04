#https://school.programmers.co.kr/learn/courses/30/lessons/131127
from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_dic = dict()
    for i in range(len(want)):
        want_dic[want[i]] = number[i]

    for i in range(len(discount) - (sum(number)-1)):
        if want_dic == Counter(discount[i:i+sum(number)]):
            answer += 1
    
    return answer

solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])