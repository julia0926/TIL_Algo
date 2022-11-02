from collections import defaultdict
from email.policy import default
import re
from typing import Counter, List

def get_new_arr(num):
    piv = 0
    pow_num = 1
    while num >= piv:
        piv = pow(2, pow_num)
        pow_num += 1
    return piv

def solution(queries: List[List[int]]) -> int:
    dic = defaultdict(int) #배열번호: 원소의 수 
    arr_size = defaultdict(int) #배열의 크기 
    result = 0
    for num, add_count in queries:
        #배열번호가 기존에 없으면 
        dic[num] += add_count #원소를 추가 !! 
        #원소의 수 , 배열 크기 비교 
        new_arr_size = get_new_arr(dic[num]) #거듭제곱 중 가장 작은 값 ! 
        # arr_size[num] = pow_num
        # if num not in dic.keys():
            
        # else: 
        #기존 배열이랑 새로운 배열 비교 
        if arr_size[num] < new_arr_size: #기존 pow < 지금 pow 기존 배ㅕㅇㄹ에 dic[num]을 복사 한 후 원소 추가                 
            print(arr_size[num], new_arr_size, "복사 안일어남")
            arr_size[num] += new_arr_size

            # else:
            #     if 
            # else:
            #     result += dic[num]
        if dic[num] > new_arr_size:
            print(dic[num], new_arr_size, "복사 일어남")
            result += dic[num]
            
                
          
                
            
           

        # else: #0 < 16 
            
             #새로운 배열로 복사

    print(result)
            
        #배열번호가 기존에 잇으면 



    answer = -1
    return answer

solution([[2,10], [7,1], [2,5], [2,9],[7,32]])