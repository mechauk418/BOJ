import sys
sys.setrecursionlimit(10**6)
d={0:0,1:1,2:1}
n=int(input())
def f(n):
    if n in d:
        return d[n]
    else:
        if n%2==0:
            k = n//2
            d[n] = (f(k)*(2*f(k-1)+f(k))) % 1000000
            return d[n]
        else:
            k = (n+1)//2
            d[n] = (f(k)**2 + f(k-1)**2) % 1000000
            return d[n]
print(f(n))