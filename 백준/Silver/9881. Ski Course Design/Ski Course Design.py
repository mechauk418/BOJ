n = int(input())
height = sorted([int(input()) for i in range(n)])
cost = [0]*n

l = 0 
r = n-1 

for i in range(n):
  if height[i] == height[0]:
    l = i

for i in range(n-1, -1, -1):
  if height[i] == height[-1]:
    r = i


while l < r and height[r] - height[l] > 17:
  l_cost = 0
  r_cost = 0

  for i in range(l+1):
    l_cost += (cost[i]+ 1)**2 - cost[i]**2

  for i in range(n-1, r-1, -1):
    r_cost += (cost[i]+1)**2 - cost[i]**2

  if l_cost < r_cost:
    for i in range(l+1):
      cost[i] += 1
      height[i] += 1
  else:
    for i in range(n-1, r-1, -1):
      cost[i] += 1
      height[i] -= 1

  for i in range(n):
    if height[i] == height[0]:
      l = i
  
  for i in range(n-1, -1, -1):
    if height[i] == height[-1]:
      r = i

print(sum([i*i for i in cost]))