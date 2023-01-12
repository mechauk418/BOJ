
N = int(input())

K = int(input())

HW = list(map(int,input().split()))

HW.sort()


M_list = []

for i in range(1,N):

    M_list.append( HW[i]-HW[i-1] )

M_list.sort(reverse=True)


M_list = M_list[K-1:]


ans = sum(M_list)

print(ans)