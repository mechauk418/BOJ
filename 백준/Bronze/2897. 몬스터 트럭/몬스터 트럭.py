R,C = map(int,input().split())

S_List = []

for i in range(R):
    S_List.append(list(input()))

ans_list = [ [9]*(C-1) for _ in range(R-1)    ]



for i in range(R-1):
    for j in range(C-1):
        check_list = [ S_List[i][j],S_List[i+1][j],S_List[i][j+1],S_List[i+1][j+1]]
        if check_list.count('#') > 0:
            ans_list[i][j] = 9999
        elif check_list.count('X') == 0:
            ans_list[i][j] = 0
        elif check_list.count('X') == 1:
            ans_list[i][j] = 1
        elif check_list.count('X') == 2:
            ans_list[i][j] = 2
        elif check_list.count('X') == 3:
            ans_list[i][j] = 3
        elif check_list.count('X') == 4:
            ans_list[i][j] = 4


one = 0
two = 0
three = 0
four = 0
five = 0

for i in range(R-1):
    one += ans_list[i].count(0)
    two += ans_list[i].count(1)
    three += ans_list[i].count(2)
    four += ans_list[i].count(3)
    five += ans_list[i].count(4)

print(one,two,three,four,five,sep='\n')