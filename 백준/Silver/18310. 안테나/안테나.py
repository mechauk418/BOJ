n = int(input())
house_li = []
house_li = list(map(int, input().rstrip().split()))
house_li.sort()
print(house_li[(n-1)//2])