def solution(n):
    k = 1
    
    while n % k != 1:
        k+=1   
    
    return k