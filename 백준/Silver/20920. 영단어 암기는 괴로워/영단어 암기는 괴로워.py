import sys
input = sys.stdin.readline

n,m = map(int, input().split())
d = {}
for _ in range(n):
	name = input().strip()
	if len(name) < m:
		continue
	if d.get(name):
		d[name][0] += 1
	else:
		d[name] = [1, len(name), name]
ans = sorted(d.items(), key= lambda x: (-x[1][0], -x[1][1], x[1][2]))

for a in ans:
	print(a[0])