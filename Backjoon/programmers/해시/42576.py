#완주하지 못한 선수 : https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

def solution(participant, completion):
    participant.sort()
    completion.sort()
    print(participant)
    print(completion)
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]


print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))