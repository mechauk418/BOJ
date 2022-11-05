


N = int(input())
R = int(input())

input_list = list(map(int,input().split()))


ans_dict = dict()

for i in range(R):

    if input_list[i] in ans_dict:
        ans_dict[ input_list[i] ][0] += 1

    else:
        if len(ans_dict) < N:
            ans_dict[input_list[i]] = [1,i]

        else:
            del_list = sorted(ans_dict.items(), key= lambda x : (x[1][0] , x[1][1]) )
            del_key = del_list[0][0]
            del(ans_dict[del_key])
            ans_dict[input_list[i]] = [1, i]

ans_list = list(sorted(ans_dict.keys()))

ans = str(ans_list[0])

for i in ans_list[1:]:

    ans += " " + str(i)

print(ans)
