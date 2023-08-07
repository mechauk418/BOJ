from collections import deque

def solution(order):
    answer = 0
    n = len(order)
    main = [ i for i in range(1,n+1)]
    main = deque(main)
    order = deque(order)
    sub = []


    for i in range(n):
        if not order:
            break

        if main[0] != order[0]:
            now = main.popleft()
            sub.append(now)

        else:
            main.popleft()
            order.popleft()
            answer +=1
            if sub:
                while sub[-1]==order[0]:
                    sub.pop()
                    order.popleft()
                    answer +=1
                    if not sub:
                        break

    return answer

order = [5,4,3,2,1]

# 1 2 5
# main = 5
# sub = [1,2]
