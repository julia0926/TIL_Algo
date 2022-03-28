def solution(clothes):
    dic = {}
    for value, sort in clothes:
        dic[sort] = dic.get(sort, 0) + 1 #헤딩 키가 없을 때 반환되는 값이 0인 것임 즉 있을 때마다 1씩 증가
    
    answer = 1
    for type in dic:
        answer *= (dic[type]+1)
    return answer - 1

solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"],  ["green_turban", "headgear"], ["yellowhat", "headgear"]]))