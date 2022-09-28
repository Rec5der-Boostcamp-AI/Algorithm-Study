def solution(n):
    num = 0
    for i in reversed(range(1,n)):
        if n % i == 1:
            num = i
            
    return num