'''
문제 : https://school.programmers.co.kr/learn/courses/30/lessons/17680
캐시교체 알고리즘(LRU) 사용 : https://hwiyong.tistory.com/398
'''

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cache_list = []
    result = 0
    for city in cities:
        if city.upper() not in cache_list: #캐시리스트에 없는 값이 들어올경우 -> Miss
            if len(cache_list) < cacheSize:
                cache_list.append(city)
            else: #캐시가 가득찼다면
                cache_list.pop(0) #가장 오래된 데이터 제거
                cache_list.append(city)
            result += 5

        else: #캐시리스트에 있는 값이 들어올경우 -> Hit!
            cache_list.pop(cache_list.index(city))
            cache_list.append(city)
            result += 1
    print(result)
    return result

def solution2(cacheSize, cities):
    import collections
    #캐시 사이즈로 덱을 만들면, append()하면 왼쪾 원소 삭제, appendleft() 하면 오른쪽 원소 삭제됨
    cache = collections.deque(maxlen=cacheSize) 
    time = 0

    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            cache.append(city) #캐시에 넣어주기만 해도, 알아서 덱이므로 가득차면 삭제하고 넣어줌 
            time += 5
    print(time)
    return time


solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution2(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])