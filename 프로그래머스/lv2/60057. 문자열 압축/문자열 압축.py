def solution(s):
    answer = []
    
    if len(s)==1:
        
        return 1

    for i in range(1,(len(s)//2)+1):
        start = s[0:i]
        cnt = 1
        new_str = ''

        for j in range(i,len(s)+i,i):
            if start == s[j:i+j]:
                cnt+=1
            else:
                if cnt !=1:
                    new_str = new_str+str(cnt)+start
                else:
                    new_str = new_str + start

                start = s[j:j+i]
                cnt = 1

        answer.append(len(new_str))

    answer = min(answer)

    return answer