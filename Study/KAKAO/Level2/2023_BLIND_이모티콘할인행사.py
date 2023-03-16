'''
1. 가입자, 2. 판매액
결과값 : [가입수, 매출액]
가입햇으면 이모티콘 구매비용 제로 

1. 각 이모티콘이 몇프로 할인할지 
'''
from itertools import product
def solution(users, emoticons):
    cases = list(product([10, 20, 30, 40], repeat=len(emoticons)))
    buy_cost = {id: 0 for id in range(len(users))}
    for case in cases:
        for id, val in enumerate(users):
            buy_list = []
            for idx, p in enumerate(case): #각 이모티콘이 할인하는 비율 
                print(">>", p, val[0])
                if p <= val[0]: #유저가 정한 비율과 비교 
                    buy_list.append(idx)
            print(buy_list)

    
    answer = []
    return answer

#할인율 이상이면 이모티콘 구매, 구매비용이 2이상이면 서비스 가입

solution([[40, 10000], [25, 10000]], [7000, 9000])
# solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])