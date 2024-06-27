N = int(input())
arr = list(map(int,input().split()))
B, C = map(int, input().split())

count = 0
sum_ = B + C 

for i in range(len(arr)):
    if B > arr[i] or B == arr[i]:
        count += 1
    elif sum_ > arr[i] or sum_ == arr[i]:
        count += 2        
    else:
        quo = (arr[i]- B) // C
        rem = (arr[i]- B) % C        
        if rem == 0:
            count += quo 
            count += 1 
        else:
            count += quo
            count += 2 

print(count)