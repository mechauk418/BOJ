fst = input()
sec = input()
thr = input()

color_list = [ 'black','brown','red','orange','yellow','green','blue','violet','grey','white'    ]
dict = {}

value = 1
for i in color_list:
    dict[i] = value
    value = value * 10

ans = int( str(color_list.index(fst)) + str(color_list.index(sec)) )

real_ans = ans * dict[thr]

print(real_ans)
