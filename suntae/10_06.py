from itertools import permutations

def solution(k, dungeons):
    result =0 
    for i in permutations(dungeons, len(dungeons)):
        k_ = k
        n = 0
        for d in i:
            if k_>= d[0]:
                k_ -= d[1]
                n +=1
            else:
                result = max(result, n)
        result = max(result,n)
    return result
