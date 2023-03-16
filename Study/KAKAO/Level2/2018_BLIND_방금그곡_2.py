def get_time(start, end):
    diff = int(end[-2:]) - int(start[-2:])
    if start[:2] == end[:2]:
        return diff
    else: #시간이 다르면
        hour = int(end[:2]) - int(start[:2])
        return (hour * 60) + diff

def replace_music(music):
    using_umm = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#':'g', 'A#':'a'}
    for i in using_umm:
        music = music.replace(i, using_umm[i])
    return music

def continue_music(music, time):
    l = len(music)
    if l < time: #재생기간이 더 길다면
        몫 = time // l
        나머지 = time % l
        music = music * 몫
        return music + music[:나머지]
    else:
        return music[:time]

def solution(m, musicinfos):
    answer = []
    for info in musicinfos:
        start, end, title, music = info.split(',')
        total_time = get_time(start, end)
        music = continue_music(music, total_time)
        m = replace_music(m)
        music = replace_music(music)
        if m in music:
            answer.append([title, total_time])

    if len(answer) == 0:
        return '(None)'
    elif len(answer) == 1:
        return answer[0][0]
    else:
        answer = sorted(answer, key=lambda x: -x[1])
        print(answer)
        return answer[0][0]

# solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
print(solution("CC#BCC#BCC#BCC#B", 	["03:00,03:30,FOO,CC#B", "03:00,03:30,FOOd2,CC#B"]))