
T = int(input())

for t in range(1,T+1):


    N = int(input())

    N_List = list(str(N))

    New_list = [str(N)]

    for i in range(len(N_List)-1):
        for j in range(i+1,len(N_List)):
            N_List[i],N_List[j] = N_List[j],N_List[i]
            if len(str(int(''.join(N_List)))) == len(str(N)):

                New_list.append( ''.join(N_List)      )
            N_List[i], N_List[j] = N_List[j], N_List[i]


    New_list = list(map(int,New_list))



    print(f'#{t} {min(New_list)} {max(New_list)}')