def solution(s):

    eng = [ 'zero','one','two','three','four','five','six','seven','eight','nine'  ]
    num = 0
    for i in eng:
        s = s.replace( i  , str(num) )
        num+=1
    s = int(s)

    return s