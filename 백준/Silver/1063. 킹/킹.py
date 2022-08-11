axis = {
    'A' : '1',
    'B' : '2',
    'C' : '3',
    'D' : '4',
    'E' : '5',
    'F' : '6',
    'G' : '7',
    'H' : '8'
}

axis_reverse = {v:k for k,v in axis.items()}

king, stone,N = input().split()
N = int(N)
start_king = ( int( axis[king[0]] ), ( int( king[1] )             )        )
start_stone = [ int( axis[stone[0]] ), ( int( stone[1] )             )        ]

move_dict = {
    'R' : (1,0),
    'L': (-1,0),
    'B': (0,-1),
    'T': (0,1),
    'RT': (1,1),
    'LT': (-1,1),
    'RB': (1,-1),
    'LB': (-1,-1)
}

x = start_king[0]
y = start_king[1]

for i in range(N):
    move = input()
    next_x = x + move_dict[move][0]
    next_y = y + move_dict[move][1]

    if next_x < 1 or next_y < 1 or next_x > 8 or next_y > 8:
        continue

    elif [next_x,next_y] == start_stone:
        if start_stone[0] + move_dict[move][0] <1 or \
            start_stone[0] + move_dict[move][0] > 8 or \
                start_stone[1] + move_dict[move][1]>8 or \
                start_stone[1] + move_dict[move][1] < 1:
            continue
        else:
            start_stone[0] = start_stone[0] + move_dict[move][0]
            start_stone[1] = start_stone[1] + move_dict[move][1]
            x = next_x
            y = next_y

    else:
        x = next_x
        y = next_y



print( f'{axis_reverse.get(str(x))}{y}')
print(f'{axis_reverse.get(str(start_stone[0]))}{start_stone[1]}')