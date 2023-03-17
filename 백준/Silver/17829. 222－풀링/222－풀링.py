
N = int(input())

arr = [ list(map(int,input().split())) for _ in range(N) ]

def divide(size,x,y):

    if size==2:
        ans = [ arr[x][y],arr[x+1][y],arr[x][y+1],arr[x+1][y+1]    ]

        ans.sort()

        return ans[-2]

    area1 = divide(size//2,x,y)
    area2 = divide(size//2, x+size//2, y)
    area3 = divide(size//2, x, y+size//2)
    area4 = divide(size//2, x+size//2, y+size//2)

    ans = [ area1,area2,area3,area4 ]

    ans.sort()

    return ans[-2]

print(divide(N,0,0))