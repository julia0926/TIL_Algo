# p.472  

from itertools import count

n, m = 5, 5 #데이터 개수, 찾고자 하는 부분 합
data = [1,2,3,2,5]

result = 0
interver_sum = 0
end = 0

for start in range(n):
    while interver_sum < m and end < n:
        interver_sum += data[end]
        end += 1
    
    #부분합이 원하는 m이라면
    if interver_sum == m:
        result += 1
    #start를 증가시키면 부분합의 범위가 줄어들므로 빼야함 
    interver_sum -= data[start] 

print(result)