import sys
input = sys.stdin.readline

dic = {}
n, m = map(int, input().split())

for _ in range(n) :
    word = input().strip()
    dic[word] = 0

for _ in range(m) :
    temp = list(map(str, input().strip().split(',')))
    for i in temp :
        if i in dic :
            del dic[i]

    print(len(dic))
