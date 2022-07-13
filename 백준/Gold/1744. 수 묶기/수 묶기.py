import sys

N=int(sys.stdin.readline())
Plus=[]
Minus=[]
merge=[]
sumnum=0
sum1=0
for i in range(N):
    K=int(sys.stdin.readline())
    if K>0:
        Plus.append(K)
    else:
        Minus.append(K)


Plus.sort(reverse=True)
Minus.sort()

for i in range(0,len(Plus),2):

    if i+1<len(Plus):
        T_num=Plus[i]*Plus[i+1]
        if T_num > Plus[i]+Plus[i+1]:
            sumnum+=T_num
        else:
            sumnum+=Plus[i]+Plus[i+1]
    else:
        merge.append(Plus[i])

for i in range(0,len(Minus),2):

    if i+1<len(Minus):
        M_num=Minus[i]*Minus[i+1]
        if M_num > Minus[i]+Minus[i+1]:
            sumnum+=M_num
        else:
            sumnum+=Minus[i]+Minus[i+1]
    else:
        merge.append(Minus[i])

merge_num=sum(merge)
sumnum=sumnum+merge_num

print(sumnum)
