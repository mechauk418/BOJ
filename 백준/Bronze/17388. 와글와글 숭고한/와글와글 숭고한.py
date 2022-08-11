S,K,H = map(int,input().split())

if S+K+H >= 100:
    print('OK')
else:
    min_uni = min(S,K,H)

    if min_uni == S:
        print('Soongsil')
    elif min_uni == K:
        print("Korea")
    else:
        print('Hanyang')