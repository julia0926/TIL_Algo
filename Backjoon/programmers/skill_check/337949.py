from distutils import command


def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0]
        end = commands[i][1]
        print(array[start:end].index())


    return answer

print(solution("[1, 5, 2, 6, 3, 7, 4]",[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))