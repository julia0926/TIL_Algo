#https://school.programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    def shap_to_lower(s):
        return s.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    
    #재생시간을 계산하는 함수
    def calculate_time(start, end):
        if start[:2] == end[:2]: #시간이 같다면
            return int(end[3:]) - int(start[3:])
        else:
            diff_hour = int(end[:2]) - int(start[:2])
            diff_min = (diff_hour * 60) + int(end[3:])
            return diff_min - int(start[3:])

    #재생시간만큼 끊임없이 음악을 반복하기 위한 함수
    def play_sound_change(sound, play_time):
        if len(sound) < play_time:  #음악 < 재생시간 = 끊임없이 처음부터 반복 
            몫 = play_time // len(sound)
            나머지 = play_time % len(sound)
            new_sound = sound * 몫 + sound[:나머지]
            return new_sound
        else: #아니라면
            return sound[:play_time] #처음 ~ 재생

    data = []
    for info in musicinfos:
        start, end, title, sound = info.split(',')
        play_time = calculate_time(start, end)
        # 재생 
        sound = shap_to_lower(sound)
        new_sound = play_sound_change(sound, play_time)
        #멜로디가 일치하는지 확인해야함
        if shap_to_lower(m) in new_sound:
            data.append([play_time, new_sound, title])

    if not data: #값이 하나도 없다면
        return '(None)'
    elif len(data) == 1: #값이 하나라면 정렬필요없이 하나 바로 리턴 
        return data[0][2]
    else:
        data.sort(key=lambda x: -x[0]) #재생시간이 제일 긴 순으로 정렬
        return data[0][2]
    
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC" ,["12:00,12:10,HELLO,ABC#ABC#ABC"] ))
print(solution("C#C", ["12:00,12:06,HELLO,C#C#CC#"] ))
print(solution("ABC",	["12:00,12:14,HELLO,C#DEFGAB","12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF","13:00,13:05,WORLD,ABCDEF"]))