def solution(n, l, r):
    answer = 0
    l-=1
    a=b=0

    def f(x):
        for i in range(20,-1,-1):
            if 5**i<=x:
                break
        t=x//(5**i)
        if t==2:
            x=0
        if t>2:
            t-=1
        return (4**i)*t, x%(5**i) 
    
    while l or r:
        a1,l = f(l)
        b1,r = f(r)
        a += a1
        b += b1
    return b-a