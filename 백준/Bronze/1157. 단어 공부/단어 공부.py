S=list(input())
count1=[]

for i in range(len(S)):
    S[i]=S[i].upper()


for i in range(26):
    count1.append( S.count(chr(i+65))  )


Alpa= count1.index(max(count1))

if count1.count(max(count1)) > 1:
    print('?')
else:
    print(chr(Alpa+65))