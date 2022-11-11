n, y, x = map(int,input().split())
count = 0

while n>0:
    val = pow(2,n) // 2 # 2^n X 2^n 배열의 중간값 
    #몇 사분면인지 알아내서 시작 값을 0행 0열로 바꿔준다.
    if n > 1: 
        # if r < val and c < val:
        #     그대로 1사분면이니까
        if y < val and x >=val: # 2사분면
            count += val**2  #1사분면 굳이 확인 안하고 값만 더함
            x -= val
        if y >= val and x < val: #3사분면
            count += (val**2) * 2
            y -=val
        if y >= val and x >=val: #4사분면
            count += (val**2) * 3
            x -= val
            y -= val

    if n == 1: #2 X 2 배열일 때
        if x==1 and y==0:
            count+=1
        elif x==0 and y==1:
            count+=2
        else:
            count+=3

    n-=1 #n을 줄이면서 범위를 줄임 

print(count)

    


