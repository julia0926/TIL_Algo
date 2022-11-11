import enum


list_num = [1,2,3,4,3,2,4]
#print(list_num.index(max(list_num)))

# answer = []
# for i in range(len(list_num)):
#     if list_num[i] == max(list_num):
#         answer.append(i + 1)


m = max(list_num)
answer = [index + 1 for index, val in enumerate(list_num) if val == m]
print(answer)