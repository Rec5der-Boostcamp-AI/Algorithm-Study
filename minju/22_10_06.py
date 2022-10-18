from itertools import permutations

def solution(k, dungeons):
    answer = 0
    len_dungeons = len(dungeons)
    for permu in permutations(dungeons, len_dungeons): 
        # print(permu)
        temp_k = k  
        count = 0  
        for p in permu:
            if temp_k >= p[0]:  
                temp_k -= p[1]  
                count += 1 
        answer = max(answer, count)  
        # print(answer)
    return answer