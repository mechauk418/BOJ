import sys

T = int(input())


def per(S,left,right):

    while left<right:
        if S[left]==S[right]:
            left+=1
            right+=-1
        else:
            return False

    return True

def secper(S,left,right):

    if S==S[::-1]:
        return 0

    while left<right:
        if S[left]==S[right]:
            left+=1
            right+=-1
        elif S[left]!=S[right]:
            start_left = per(S,left+1,right)
            start_right = per(S,left,right-1)

            if start_right or start_left:
                return 1
            else:
                return 2


for t in range(T):
    S = sys.stdin.readline().rstrip()

    left = 0
    right = len(S)-1

    print(secper(S,left,right))