#https://leetcode.com/problems/jewels-and-stones/submissions/

from collections import defaultdict

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = defaultdict(int)
        count = 0
        #돌 세기
        for s in stones:
            freq[s] += 1
        
        for j in jewels:
            count += freq[j]

        return count
                
    def numJewelsInStones2(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
