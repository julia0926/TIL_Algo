#https://school.programmers.co.kr/learn/courses/30/lessons/155651
import heapq
def solution(book_time):

    def change_to_minute(time):
        hour, minute = map(int, time.split(":"))
        hour *= 60
        return hour + minute

    all_list = []
    for time in book_time:
        start, end = change_to_minute(time[0]), change_to_minute(time[1])
        all_list.append([start, end])

    all_list = sorted(all_list, key=lambda x: x[0]) #시작시간
    end_list = []
    result = 0
    for start, end in all_list:
        if not end_list or end_list[0] > start: #방의 제일 빠른시간의 끝시간 > 현재 시작점
            heapq.heappush(end_list, end+10)
            result += 1
        elif end_list[0] <= start: #방의 제일 빠른시간의 끝시간 <= 현재 시작점
            heapq.heappop(end_list)
            heapq.heappush(end_list, end+10)
        
    return result


solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])