from itertools import permutations

def solution(users, emoticons):
    sale_arr = [0] * len(emoticons)
    member, salse = 0, 0
    #최대 가입자 찾기 
    def max_users():
        for percent, price in users:
            buy_price = 0
            for sale in sale_arr:
                if sale > percent

    #할인율 조합 
    def sale_combi(idx):
        if id == len(emoticons):
            max_users()
            return
        for i in range(10, 41, 10):
            sale_arr[idx] = i
            sale_combi(idx+1)

    # sale_combi(0)
    max_users()
    # sale_combi(0)
    answer = []
    return answer

solution([[40, 10000], [25, 10000]], [7000, 9000])