import sys

X,Y = map(int,sys.stdin.readline().split())


Z = int((100*Y/X))

start = 1
end = X
ans=0
while start <= end:

    if Z>=99:
        ans=-1
        break


    mid = (start+end)//2

    WinRate = int((100*(Y+mid)/(X+mid)))


    if WinRate == Z:

        start = mid+1

    else:
        ans = mid
        end = mid -1


print(ans)
