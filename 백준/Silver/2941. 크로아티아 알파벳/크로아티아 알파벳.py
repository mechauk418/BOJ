N=input()
S=['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in range(len(S)):
    if S[i] in N:

        N=N.replace(S[i],'5')



print(len(N))
