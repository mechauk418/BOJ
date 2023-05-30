
N = int(input())

tree= dict()

for i in range(N):

    root,left,right = input().split()

    tree[root] = [left,right]



def pre(x):
    if x=='.':
        return

    else:
        left,right = tree[x]
        print(x,end="")
        pre(left)
        pre(right)


def mid(x):
    if x=='.':
        return

    else:
        left,right = tree[x]
        mid(left)
        print(x, end="")
        mid(right)


def back(x):
    if x=='.':
        return

    else:
        left,right = tree[x]
        back(left)
        back(right)
        print(x, end="")


pre('A')
print()
mid('A')
print()
back('A')