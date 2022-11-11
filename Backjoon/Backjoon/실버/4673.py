# 생성자가 

n = 75
self_arr = []
def selfnumber(n):
    if n == 10000:
        return self_arr
    l = len(str(n))
    stn = str(n)
    sum_val = n
    for i in range(l):
        sum_val += int(stn[i])
    self_arr.append(sum_val)
    selfnumber(sum_val)
print(selfnumber(75))
