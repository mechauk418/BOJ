import copy

def solution(beginning, target):
    graph =[[] for _ in range(len(beginning)) ]


    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if beginning[i][j]==target[i][j]:
                graph[i].append(0)
            else:
                graph[i].append(1)

    graph2=copy.deepcopy(graph)
    graph3 = copy.deepcopy(graph)
    graph4 = copy.deepcopy(graph)

    cnt1=0
    cnt2=0
    cnt3=0
    cnt4=0

    # 행 먼저

    for i in range(len(beginning)):
        if graph[i][0]==1:
            cnt1+=1
            for j in range(len(beginning[0])):
                graph[i][j]=1-graph[i][j]

    for i in range(len(beginning[0])):
        if graph[0][i]==1:
            cnt1+=1
            for j in range(len(beginning)):
                graph[j][i]=1-graph[j][i]

    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if graph[i][j]==1:
                cnt1 = -1
                break

    # 열 먼저
    for i in range(len(beginning[0])):
        if graph2[0][i]==1:
            cnt2+=1
            for j in range(len(beginning)):
                graph2[j][i]=1-graph2[j][i]

    for i in range(len(beginning)):
        if graph2[i][0]==1:
            cnt2+=1
            for j in range(len(beginning[0])):
                graph2[i][j]=1-graph2[i][j]

    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if graph2[i][j]==1:
                cnt2 = -1
                break

    # 행 먼저


    for i in range(len(beginning)):
        if graph3[i][0]==0:
            cnt3+=1
            for j in range(len(beginning[0])):
                graph3[i][j]=1-graph3[i][j]

    for i in range(len(beginning[0])):
        if graph3[0][i]==1:
            cnt3+=1
            for j in range(len(beginning)):
                graph3[j][i]=1-graph3[j][i]

    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if graph3[i][j]==1:
                cnt3 = -1
                break

    # 열 먼저
    for i in range(len(beginning[0])):
        if graph4[0][i]==0:
            cnt4+=1
            for j in range(len(beginning)):
                graph4[j][i]=1-graph4[j][i]

    for i in range(len(beginning)):
        if graph4[i][0]==1:
            cnt4+=1
            for j in range(len(beginning[0])):
                graph4[i][j]=1-graph4[i][j]

    for i in range(len(beginning)):
        for j in range(len(beginning[0])):
            if graph4[i][j]==1:
                cnt4 = -1
                break

    if (cnt1 == -1) or (cnt2==-1) or (cnt3==-1) or (cnt4==-1):
        answer = -1
    else:
        answer = min(cnt1,cnt2,cnt3,cnt4)
    return answer
