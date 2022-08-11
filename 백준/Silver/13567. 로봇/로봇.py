M,n = map(int,input().split())


x = 0
y = 0
dir_list = [ [1,0], [0,1],[-1,0],[0,-1]  ]
turn_cnt = 0


dir = dir_list[0]

for i in range(n):
    cmd,num = map(str,input().split())
    num = int(num)

    if cmd == 'TURN' and num == 0:
        turn_cnt +=1
        dir = dir_list[ turn_cnt%4    ]
    elif cmd == 'TURN' and num == 1:
        turn_cnt -=1
        dir = dir_list[ turn_cnt%4    ]
    else:
        if dir[0] != 0:
            next_x = x + dir[0] * num
            if next_x < 0 or next_x > M:
                print(-1)
                break
            else:
                x = next_x
        elif dir[1] != 0:
            next_y = y + dir[1] * num
            if next_y < 0 or next_y > M:
                print(-1)
                break
            else:
                y = next_y

else:
    print(x,y)



