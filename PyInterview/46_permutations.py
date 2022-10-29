def permute(arr):
    result = []
    pre = []
    def dfs(elements):
        print("dfs!!!")
        if len(elements) == 0:
            result.append(pre[:])
            print("result append", pre)
        for e in elements:
            next = elements[:] #복사한다
            next.remove(e) 
            print("next", next)

            pre.append(e)
            print("pre", pre)
            dfs(next) #지운 값을 기준으로 깊이우선탐색
            print("---pre pop")
            pre.pop()
    dfs(arr)
    return result

print(permute([1,2]))
