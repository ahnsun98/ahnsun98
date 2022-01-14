def solution(N, stages):
    answer = []
    failrate = []
    stages.sort()
    for i in range(1,N+1):
        fail = stages.count(i)
        reach = 0
        for s in stages:
            if(s >= i):
                reach += 1
        if reach:
            failrate.append([i,fail/reach])
        else:
            failrate.append([i,0])
    
    failrate.sort(key=lambda x:(-x[1],x[0]))
    answer = [f[0] for f in failrate]
    return answer

N = 4
stages = [4,4,4,4,4]
answer = solution(N, stages)
print(answer)
