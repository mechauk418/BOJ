
T=int(input())

buffer = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
          's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']


for i in range(T):

    S=input()
    ans=''
    for k in S:
        value = buffer.index(k)
        value_2 = bin(value)[2:]
        while len(value_2) < 6:
            value_2 = '0' + value_2

        ans += value_2
    bin_list=[]
    for k in range(len(ans)//8):
        bin_num = ans[8*k:8*(k+1)]
        int_num = int(bin_num,2)
        int_num = chr(int_num)
        bin_list.append(int_num)
    ans_m = ''.join(bin_list)
    print(f'#{i+1} {ans_m}')
