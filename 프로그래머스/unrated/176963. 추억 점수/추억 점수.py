def solution(name, yearning, photo):
    info = dict()
    for n, y in zip(name, yearning):
        info[n] = y
    result = []
    for pt in photo:
        count = 0
        for p in pt:
            if p in list(info.keys()):
                count += info[p]
        result.append(count)
     
    
    return result