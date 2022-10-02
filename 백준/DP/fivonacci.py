def fivonacci(num):
    if num == 1 or num == 2:
        return 1
    return fivonacci(num-1) + fivonacci(num-2)

print(fivonacci(4))

#Memoriztion : 한번 계산된 결과는 저장한다. 
d = [0] * 100 #미리 계산될 값을 저장함.

def top_down(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0: #계산된 적이 있으면
        return d[x]
    d[x] = top_down(x-1) + top_down(x-2)
    return d[x]

top_down(4)

#bottom_up 방식
d = [0, 1, 1] + [0] * 98
n = 98

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d)
