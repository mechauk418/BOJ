import sys

N=int(sys.stdin.readline())
A,B,C,D,E,F=map(int,sys.stdin.readline().split()) # 문제 입력

dict_num_ori={ 'A':A,'B':B,'C':C,'D':D,'E':E,'F':F}

dict_num={ 'A':A,'B':B,'C':C,'D':D,'E':E,'F':F}

min_num=min(dict_num,key=dict_num.get)

max_num=max(dict_num_ori.values()) # N이 1일때를 위해 최대값을 찾아준다.


if min_num=='A' or min_num== 'F' :
    del dict_num['F']
    del dict_num['A']
    min_num2 = min(dict_num, key=dict_num.get)
    if min_num2 == 'B'or min_num2=='E':
        del dict_num['B']
        del dict_num['E']
        min_num3 = min(dict_num, key=dict_num.get)
    else:
        del dict_num['C']
        del dict_num['D']
        min_num3 = min(dict_num, key=dict_num.get)


elif min_num=='B'or min_num== 'E':
    del dict_num['E']
    del dict_num['B']
    min_num2 = min(dict_num, key=dict_num.get)
    if min_num2 == 'A' or min_num2=='F':
        del dict_num['A']
        del dict_num['F']
        min_num3 = min(dict_num, key=dict_num.get)
    else:
        del dict_num['C']
        del dict_num['D']
        min_num3 = min(dict_num, key=dict_num.get)

elif min_num=='C'or min_num=='D':
    del dict_num['D']
    del dict_num['C']
    min_num2 = min(dict_num, key=dict_num.get)
    if min_num2 == 'A' or min_num2=='F':
        del dict_num['A']
        del dict_num['F']
        min_num3 = min(dict_num, key=dict_num.get)
    else:
        del dict_num['B']
        del dict_num['E']
        min_num3 = min(dict_num, key=dict_num.get)



real_num=dict_num_ori.get(min_num)
real_num2=dict_num_ori.get(min_num2)
real_num3=dict_num_ori.get(min_num3)


block_num=N**3 # 총 블록의 갯수
block1ea=4*(N-1)*(N-2) + (N-2)**2 # 면이 1개만 계산되는 블록의 갯수
# print(block1ea)
block2ea = block_num - (block1ea + 4) - (N-1)*(N-2)*(N-2) # 면이 2개 계산되는 블록의 갯수
# print(block2ea)
ans = 4 * (real_num+real_num2+real_num3) + (block2ea)*(real_num+real_num2) + (block1ea * real_num)
# 면이 3개인 블록은 항상 4개로 고정이다.


if N==1:
    print(A+B+C+D+E+F - max_num)
else:
    print(ans)