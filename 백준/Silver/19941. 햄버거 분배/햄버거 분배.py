
n,k = map(int,input().split())

hp = list(input())

p_cnt= 0

for i in range(n):

    if hp[i]=='P':

        for j in range(max(i-k,0), min(i+k+1,n)):

            if hp[j]=='H':
                hp[j]=0
                p_cnt+=1
                break


print(p_cnt)