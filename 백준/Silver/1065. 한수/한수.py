def hansu(N):
    count = 9

    if N<10:
        return N

    for i in range(N+1):
        i=str(i)
        N_list=[]
        Minus = []


        for j in range(len(i)):
            N_list.append(int(i[j]))

        for k in range(len(i)-1):
            Minus.append(N_list[k+1]-N_list[k])


        if len(set(Minus))==1:
            count+=1



    return count

N=int(input())
print(hansu((N)))