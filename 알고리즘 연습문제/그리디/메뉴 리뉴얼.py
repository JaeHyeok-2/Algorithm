#   https://programmers.co.kr/learn/courses/30/lessons/72411

from collections import Counter
from itertools import combinations


def solution(orders, courses):
    answer = []

    for course in courses:
        candidates = []
        for menuList in orders:
            for li in combinations(menuList, course):
                res = ''.join(sorted(li))
                candidates.append(res)
        sorted_candidates = Counter(candidates).most_common()
        # print(sorted_candidates)
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)