#미해결
def solution(babbling):
    answer = 0
    temp = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        count = 0
        for k in range(len(temp)):
            if b == temp[k]:
                answer+=1
                break
            b1 = b.split(temp[k])
            if len(b1) > 1:
                n = b1.count("")
                if n == 0:
                    n = 1
                count = count + len(temp[k]) * n
        if count == len(b):
            answer += 1
    return answer