#내 시도 실패
# def lengthOfLongestSubstring(s):
#     count = 0
#     arr = []
#     result = []
#     for char in s:
#         if char in arr:
#             result.append(count)
#             count = 1
#             arr = [char]
#         else:
#             arr.append(char)
#             count += 1
#     if count != 0:
#         result.append(count)
#     print(result)
#     return max(result) if result else 0

#슬라이딩 윈도우 
def lengthOfLongestSubstring(s):
    max_len = 0
    start, end = 0, 0 #투포인터를 하기 위해 start, end를 
    chars = {} #중복 문자를 체크하기 위함
    while end < len(s):
        if s[end] in chars: #중복 문자가 있다면
            chars.remove(s[start]) #중복문자를 set에서 제거하고
            start += 1 #start 인덱스를 올림
        else: #중복 문자가 없다면
            chars.add(s[end]) #문자를 set에 넣고
            max_len = max(max_len, end-start+1) #기존 max와 현재 부분문자열 길이 비교
            end += 1 #end 증가
    return max_len




print(lengthOfLongestSubstring("abcabcbb"))