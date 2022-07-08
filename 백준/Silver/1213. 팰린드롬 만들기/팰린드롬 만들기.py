import sys, collections

S=sys.stdin.readline().rstrip()

S_list=list(S)
dict1={}
#print(S_list)
dict1=collections.Counter(S_list)
dict1=dict(sorted(dict1.items()))

#print(dict1)

L_list=list(dict1.keys())
C_list=list(dict1.values())

#print(L_list)
#print(C_list)
odd=''
odd_count=0
for i in range(len(C_list)):
    if C_list[i]%2==1:
        odd = i
        odd_count+=1
        C_list[i]=int((C_list[i]-1)*0.5)

    else:
        C_list[i]=int(C_list[i]*0.5)

#print(C_list)
ans=''
for i in range(len(C_list)):
    ans+=L_list[i]*C_list[i]


ans_list=list(ans)
ans_list.reverse()
ans2=''.join(ans_list)

if odd_count>1:
    print('I\'m Sorry Hansoo')
elif type(odd)==int:
    print(ans,L_list[odd],ans2,sep='')
else:
    print(ans,ans2,sep='')
