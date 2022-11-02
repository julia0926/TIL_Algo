# p.138 : https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = []
        for i in s.lower():
            if i.isalnum():
                str.append(i)
                
        while len(str) > 1:
            if str.pop(0) != str.pop():
                return False
            
        return True