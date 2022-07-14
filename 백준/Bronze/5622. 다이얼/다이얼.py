N=input()
ans=0
for i in N:
    if i in ['A','B','C']:
        ans+=3
    elif i in ['D','E','F']:
        ans+=4
    elif i in ['G','H','I']:
        ans+=5
    elif i in ['J','K','L']:
        ans+=6
    elif i in ['M','N','O']:
        ans+=7
    elif i in ['P','Q','R','S']:
        ans+=8
    elif i in ['T','U','V']:
        ans+=9
    else:
        ans+=10


print(ans)

