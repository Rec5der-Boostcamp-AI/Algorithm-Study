def solution(survey, choices):
    answer = ''
    lst = ['R','T','C','F','J','M','A','N']
    num_list = [0 for _ in range(8)]
    
    
    for i in range(len(choices)):
        if choices[i] == 4:
            continue
        
        elif choices[i] > 4:
            num_list[lst.index(survey[i][1])] += (choices[i] - 4)
            
        elif choices[i] < 4:
            num_list[lst.index(survey[i][0])] += (4 - choices[i])
            
    
    for i in range(0,len(num_list),2):
        
        if num_list[i] > num_list[i+1]:
            answer += lst[i]
            
        elif num_list[i] < num_list[i+1]:
            answer += lst[i+1]
        
        else:
            if lst[i] < lst[i+1]:
                answer += lst[i]
            else:
                answer += lst[i+1]
    
    return answer