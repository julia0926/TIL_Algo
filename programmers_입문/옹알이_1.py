import re
def solution(babbling):
    pronunciation = ["aya", "ye", "woo", "ma"]
    result = 0
    for bab in babbling:
        temp = re.sub('aya|ye|woo|ma', '', bab)
        if temp == "":
            result += 1
    return result

# solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])
print(solution(["aya", "yee", "u", "maa", "wyeoo"]))