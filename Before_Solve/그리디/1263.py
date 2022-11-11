n = int(input())
list = []
for _ in range(n):
    t, s = map(int,input().split()) 
    list.append([s, t]) #s시간 내에 처리해야 하고, t시간이 소요됨

list.sort(reverse=True) #작업 완료시간으로 정렬
now_time = list[0][0] - list[0][1] #15
#시작시간 갱신 
for i in range(1, n):
    if now_time <= list[i][0]: #현재는 15시인데 16시나 15시까지 해야된다면 
        now_time -= list[i][1]
    else: 
        now_time = list[i][0] - list[i][1] 
        #현재는 15시인데 12시까지 해야된다면 12~15시 비어있고 12시를 시작으로 t시간 빼서 시작시간 갱신
print(now_time if now_time>=0 else -1)
