#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def letterCombinations(digits):
    result = []
    phone_dic = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }

    def dfs(idx, path): 
        if idx == len(digits):
            result.append(path)
            return
        for i in range(idx, len(digits)): #하나의 path에 몇개
            for j in phone_dic[int(digits[i])]: #path뒤에 값 붙임 
                dfs(i+1, path+j)

    if not digits:
        return []
    dfs(0, "")
    return result

print(letterCombinations("23"))

            