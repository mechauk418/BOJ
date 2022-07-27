S=input()

cnt = 0
cnt_left = 0
cnt_right = 0

for i in range(len(S)):
    if S[i] == '@':
        cnt +=1
    elif S[i] == '(':
        cnt_left = cnt
        cnt = 0

cnt_right = cnt

print(cnt_left, cnt_right)


