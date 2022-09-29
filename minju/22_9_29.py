def solution(survey, choices):
    answer = ''
    score = {1 : 3, 2:2,3:1,4:0,5:1,6:2,7:3}
    q = {1:["R","T"],2:["C","F"],3:["J","M"],4:["A","N"]}
    me = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    
    for i in range(len(survey)):
        if choices[i] < 4: #4점 기준으로 점수 매김
            me[survey[i][0]] += score[choices[i]]
            
        else:
            me[survey[i][1]] += score[choices[i]]
    
    for key, value in q.items():#지표별 성격 유형 점수 비교
        if me[value[0]] >= me[value[1]]:
            answer+=value[0]
        else:
            answer+=value[1]        
    return answer