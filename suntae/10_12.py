def check(word,last):
    l = len(last)
    if len(word) ==1:
        return 0
    
    if len(word) == 0:
        return 1
    
    if word[0:l] == last:
        return 0
    else:
        if word[0:2] == "ye":
            return check(word[2::],"ye")
        elif word[0:2] == "ma":
            return check(word[2::],"ma")
        elif word[0:3] == "woo":
            return check(word[3::],"woo")
        elif word[0:3] == "aya":
            return check(word[3::],"aya")
        else:
            return 0


def solution(babbling):
    answer = 0
    for bab in babbling:
        answer += check(bab,"!")

    return answer
