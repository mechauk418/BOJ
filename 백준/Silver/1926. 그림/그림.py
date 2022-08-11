import sys
sys.setrecursionlimit(10**6)

h,w = map(int, input().split())

size_list = []

S_graph = [list(map(int, input().split())) for _ in range(h)]  # 그래프 선언

def dfs(x, y):
    if x <= -1 or x >= h or y<=-1 or y>=w:  # 경계조건
        return False

    if S_graph[x][y] == 1:  # 그래프 요소가 1이면 0으로 바꿔준다
        S_graph[x][y] = 0
        global size
        size +=1



        #인접한 8방향 요소에도 반복

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)


        return True  # 1을 0으로 바꿨으면 True를 반환



    return False  # 바꾸지 않았따면 False를 반환

cnt = 0
size = 0

for i in range(h):
    for j in range(w):
        if dfs(i, j) == True:  # 해당 연결요소를 처음으로 만날때 카운트를 해준다
            size_list.append(size)
            size = 0
            cnt += 1


print(cnt)
if len(size_list) >0:
    print(max(size_list))
else:
    print(0)