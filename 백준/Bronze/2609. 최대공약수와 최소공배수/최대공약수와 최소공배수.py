
A,B = map(int,input().split())

Ori_A = A
Ori_B = B

while B!=0:
    r = divmod(A,B)[1]
    A = B
    B = r

GCD = A
LCM = int(Ori_A * Ori_B / GCD)
print(GCD)
print(LCM)