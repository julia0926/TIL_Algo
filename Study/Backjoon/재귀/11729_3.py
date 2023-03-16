n = int(input())

#원판 n개를 a->b로 옮기는 방법
def move(a, b, n): 
    if n == 1:
        print(a, b)
        return
    move(a, 6-a-b, n-1) #1->2 
    print(a,b)
    move(6-a-b, b,n-1) #2->3

print(pow(2, n)-1) #하노이탑 이동순서 점화식
move(1, 3, n)
