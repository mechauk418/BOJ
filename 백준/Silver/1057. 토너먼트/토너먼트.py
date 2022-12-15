# A 김지민
# B  임한수
import sys

N,A,B = map(int,sys.stdin.readline().split())

count = 0

while True:

    A = A - (A//2)
    B = B - (B//2)

    count+=1

    if A==B:
        break


print(count)

