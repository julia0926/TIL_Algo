from typing import List

def solution(k: int, dic: List[str], chat: str) -> str:
    chat_list = chat.split()
    for idx, str in enumerate(chat_list):
        if str in dic:
            chat_list[idx] = "#" * len(str)
        
        

    print(chat_list)
    answer = ''
    return answer

solution(2, ["slang", "badword"], "badword ab.cd bad.org .word sl.. bad.word")