
def solution(info, edges):
    answer = []
    n = len(info)
    visited = [0] * n

    def dfs(sheep,wolf):
        if sheep>wolf:
            answer.append(sheep)
        else:
            return
        for i,j in edges:

            if visited[i] and not visited[j]:
                visited[j]=1
                if info[j]==0:
                    dfs(sheep+1,wolf)
                else:
                    dfs(sheep,wolf+1)
                visited[j] = 0
    visited[0]=1
    dfs(1,0)

    ans = max(answer)
    return ans