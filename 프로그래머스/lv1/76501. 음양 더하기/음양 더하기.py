def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == True :
            absolutes[i] = absolutes[i]
        else:
            absolutes[i] = -absolutes[i]

    return sum(absolutes)

