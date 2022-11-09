from collections import deque

def solution(ingredient):
    answer = 0
    ing = deque(ingredient[0:3])
    for i in range(3,len(ingredient)):
        ing.append(ingredient[i])
        if len(ing) > 3:
            if [ing[-4],ing[-3],ing[-2],ing[-1]] == [1,2,3,1]:
                for j in range(4):
                    ing.pop()
                answer +=1   

    return answer
