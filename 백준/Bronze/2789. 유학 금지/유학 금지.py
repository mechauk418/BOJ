N=input()
S=['C','A','M','B','R','I','D','G','E']

for i in range(len(S)):
    if S[i] in N:

        N=N.replace(S[i],'')


print(N)

