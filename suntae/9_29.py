def solution(survey, choices):
    dic = {}
    dic["RT"] = 0
    dic["CF"] = 0
    dic["JM"] = 0
    dic["AN"] = 0
    
    for i in range(len(survey)):
        if survey[i] in dic:
            dic[survey[i]] += choices[i]-4
        else:
            dic[survey[i][1]+survey[i][0]] -= choices[i]-4
    answer = ""
    for point in dic:
        if dic[point] <=0:
            answer += point[0]
        elif dic[point] >0:
            answer += point[1]

    return answer
