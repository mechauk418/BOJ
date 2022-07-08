# [Silver III] 팰린드롬 만들기 - 1213 

[문제 링크](https://www.acmicpc.net/problem/1213) 

### 성능 요약

메모리: 32452 KB, 시간: 92 ms

### 분류

그리디 알고리즘(greedy), 구현(implementation), 문자열(string)



### 풀이



팰린드롬을 만들기위해서는 문자의 갯수를 카운팅했을때 홀수인 문자가 없거나 1개만 존재해야하며 2개 이상일 경우 I'm sorry hansoo를 출력해준다.

또한, 홀수가 1개인 경우 그 문자 1개가 가운데로 와야한다.



파이썬 collections 내장함수의 Conuter 을 사용하면 리스트 요소와 그 갯수를 딕셔너리로 반환해준다.

```python
import sys, collections

S=sys.stdin.readline().rstrip()

S_list=list(S)
dict1={}
dict1=collections.Counter(S_list) # 리스트의 요소와 갯수를 딕셔너리로 반환
dict1=dict(sorted(dict1.items())) # 딕셔너리 사전순서로 정렬

L_list=list(dict1.keys()) # 문자 리스트
C_list=list(dict1.values()) # 문자의 갯수 리스트

odd='' # 홀수를 찾기위한 변수 선언
odd_count=0 # 홀수의 갯수를 측정
for i in range(len(C_list)):
    if C_list[i]%2==1:
        odd = i # 갯수가 홀수개인 문자가 가운데로 와야하므로 인덱스를 기억한다
        odd_count+=1
        C_list[i]=int((C_list[i]-1)*0.5)

    else:
        C_list[i]=int(C_list[i]*0.5)

ans=''
for i in range(len(C_list)):
    ans+=L_list[i]*C_list[i]


ans_list=list(ans) # 뒷부분 완성을 위해 역순으로 정렬함
ans_list.reverse()
ans2=''.join(ans_list)

if odd_count>1:
    print('I\'m Sorry Hansoo')
elif type(odd)==int:
    print(ans,L_list[odd],ans2,sep='')
else:
    print(ans,ans2,sep='')
```



