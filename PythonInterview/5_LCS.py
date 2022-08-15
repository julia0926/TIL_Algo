def expand(left, right, str):
    while left >= 0 and right < len(str) and str[left] == str[right]:
        left -= 1
        right += 1
    return str[left+1:right ]


def longestPalindrome(str):
    if str == str[::-1] or len(str) < 2:
        return str
    
    result = ''
    # 슬라이딩 윈도우
    for i in range(len(str)-1):
        result = max(result, expand(i, i+1, str), expand(i, i+2, str), key=len)
    print(result)

longestPalindrome("cbbd")
longestPalindrome("babad")
    
    
