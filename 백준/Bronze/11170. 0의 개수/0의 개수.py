
T = int(input())

for t in range(T):
    N,M = map(int,input().split())
    ans = [str(i).count('0') for i in range(N,M+1) if '0' in str(i)]
    print(sum(ans))

