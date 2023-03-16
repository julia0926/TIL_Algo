from re import L


def mergeTowList(l1, l2):
    result = []
    for c1, c2 in zip(l1, l2):
        result += c1, c2
    # print(result)

mergeTowList([1,2,4],[1,3,4])

def reverseList(l1, l2):
    l = reversed(l1)
    # print(l1.reverse)
    # return sum(int(l1), int(l2))

# print(reverseList([2,4,3], [5,6,4]))

list_ex = [1,2,3]
list_ex.reverse()
print(list_ex)
print(list(reversed(list_ex)))