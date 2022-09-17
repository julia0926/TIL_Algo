def solution(sizes):
    max_list, min_list = [], []
    for w, h in sizes:
        if w >= h:
            max_list.append(w)
            min_list.append(h)
        else:
            max_list.append(h)
            min_list.append(w)
    return max(max_list) * max(min_list)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))