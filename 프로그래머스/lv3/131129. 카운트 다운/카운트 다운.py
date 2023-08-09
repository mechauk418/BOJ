from collections import deque
MAX = float('inf')

def solution(target):
    dp = [[MAX, -MAX] for _ in range(target+1)]
    
    q = deque([(0, 0, 0)])
    
    while q :
        score, dart, single = q.popleft()
        
        for i in range(1, 21) :
            for j in range(1, 4) :
                _score = i*j + score
                if _score > target :
                    continue
                
                _single = single + 1 if j == 1 else single
                if dp[_score][0] > dart + 1  or dp[_score][0] == dart + 1 and dp[_score][1] < _single :
                    dp[_score] = [dart+1, _single]
                    q.append((_score, dart+1, _single))
                    
        if score + 50 > target :
            continue
        if dp[score + 50][0] > dart + 1 or dp[score+50][0] == dart + 1 and dp[score + 50][1] < single + 1 :
            dp[score+50] = [dart + 1, single + 1]
            q.append((score+50, dart+1, single+1))
        
    return dp[-1]