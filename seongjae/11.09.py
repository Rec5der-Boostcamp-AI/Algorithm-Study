
def main():
    
    #답지봄
    N = int(input())
    stair = [0]*301
    for i in range(N):
        stair[i]=int(input())

    DP = [0]*301
    DP[0] = stair[0]
    DP[1] = stair[0]+stair[1]
    DP[2] = max(stair[0]+stair[2], stair[1]+stair[2])

    for i in range(3, N):
        DP[i] = max(DP[i-3] + stair[i-1] + stair[i], DP[i-2]+stair[i])

    print(DP[N-1])



if __name__ == "__main__":
    main()

#재귀로는 실패 시간초가남
"""
    count =0
    answer =0
    answer = f(n,-1,step,count,answer)
    print(answer)
def f(n,idx,step,count,answer):
    if idx ==n-1:#도착했을 때
        answer += step[idx]
        #print("IDX = ", idx, " answer = ", answer)
        return answer
    elif idx >=n:
        #print("IDX = ", idx, " answer = ", answer, "return 0")
        return 0
    if idx != -1:
        answer += step[idx]
    #choose 1
    tmp1=0
    if count+1 <3:
        tmp1 = f(n,idx+1,step,count+1,answer)
    #choose 2
    tmp2 = f(n,idx+2,step,1,answer)
    tmp = max(tmp1,tmp2)
    return max(answer,tmp)
    """

