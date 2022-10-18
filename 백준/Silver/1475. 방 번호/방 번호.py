from collections import Counter
import math

N = int(input())

N = list(str(N))

ans_dict = dict(Counter(N))

if '6' in ans_dict and '9' in ans_dict:
    ans_dict['6']= math.ceil((ans_dict['6']+ans_dict['9'])/2)
    ans_dict['9']= ans_dict['6']


if '6' in ans_dict and '9' not in ans_dict:
    ans_dict['6']= math.ceil(ans_dict['6']/2)

if '9' in ans_dict and '6' not in ans_dict:
    ans_dict['9']= math.ceil(ans_dict['9']/2)


print(max(ans_dict.values()))