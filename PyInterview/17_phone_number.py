#https://leetcode.com/problems/letter-combinations-of-a-phone-number/
def letterCombinations(digits):
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []
    #깊이 우선 탐색을 해야 한다.
    def dfs(idx, path):
        if len(path) == len(digits): #붙인 길이와 인덱스 길이가 같으면 output
            result.append(path)
            return

        for i in range(idx, len(digits)):
            for j in dic[digits[i]]: #인풋의 dic의 키값의 문자 하나씩
                # print(i, j)
                dfs(idx+1, path+j) #인덱스는 하나씩 증가 해야하고 path는 값 하나씩 붙임 

    dfs(0, "")
    print(result)



letterCombinations("23")
        