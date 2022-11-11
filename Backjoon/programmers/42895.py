
def solution(n, number):
    #나누기를 했을 때는 먼저 계산 해야됨 
    operator = ['*','//','+','-'] #연산자
    answer = 0
    cal_num = 0
    d = [0] * 10000 #모든 경우의 수를 넣기 위한 배열 

    half_list = [0] * (number // 2 + 1) #N을 구할 수 있는 두개의 합 (ex. 12-0, 11-1, 10-2 ... 6-6)
    
    #경우의 수 (일단 1번만 )
    while cal_num == number: #계산한 값과 number이 같을 때 까지
        
        if n == number: #n을 1번 사용한 경우
            answer += 1
        elif 
        #n을 2번 사용한 경우 
        # n+n, nn, n//n, n*n 


    
    if answer >= 8:
        return -1
    return answer


print(solution(5,12))