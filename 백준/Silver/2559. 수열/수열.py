n, k = map(int,input().split())

tem = list(map(int,input().split()))

start = 0
end = k



check_num = sum(tem[start:end])

max_ans = check_num

while True:

    if end==n:
        break

    check_num += tem[end]
    check_num -= tem[start]

    if check_num > max_ans:
        max_ans = check_num

    start += 1
    end += 1


print(max_ans)