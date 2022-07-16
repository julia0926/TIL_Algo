def solution(mylist):
    #1. 일반적인 방법
    #answer = [[], [], []]
    #for i in range(len(mylist)):
    #    for j in range(len(mylist)):
    #        answer[i].append(mylist[j][i])
    #return answer

    #2. 파이썬 답게
    return list(map(list, zip(*mylist)))


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

#⭐️zip 사용 
mylist = [1, 2, 3]
new_list = [40, 50, 60]

for i in zip(mylist, new_list):
    print(i)

'''
(1, 40)
(2, 50)
(3, 60)
'''

#key, value list로 딕셔너리 만들기
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
print(dict(zip(animals, sounds))) #{'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}