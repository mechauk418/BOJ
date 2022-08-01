import sys

N = int(sys.stdin.readline())

name_dict = {}

for i in range(N):
    name = sys.stdin.readline().rstrip()
    if name in name_dict:
        name_dict[name] += 1
    else:
        name_dict[name] = 1

for i in range(N-1):
    name = sys.stdin.readline().rstrip()
    if name in name_dict:
        name_dict[name] += -1

bb = {v:k for k,v in name_dict.items()} #// {'AA': '0', 'BB': '1', 'CC': '2'}
print(bb.get(1))