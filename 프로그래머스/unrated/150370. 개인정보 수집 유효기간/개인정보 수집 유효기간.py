def solution(today, terms, privacies):
    ans = []
    term_dict = dict()
    today_year,today_month,today_day = map(int,today.split('.'))
    idx = 1
    

    for t in terms:
        alp,num = t.split()
        term_dict[alp] = int(num)
        
    term_alp = list(term_dict.keys())
    for pri in privacies:
        priday,term = pri.split()
        year,month,day = map(int,priday.split('.'))
        for alp in term_alp:
            if term ==alp:
                month+=term_dict[alp]
                while True:
                    
                    if month >12:
                        year+=1
                        month = month-12
                    else:
                        break
        
        if today_year > year:
            ans.append(idx)

        elif (year==today_year) and today_month>month:
            ans.append(idx)
        elif (year==today_year) and (today_month==month) and (today_day>=day):
            ans.append(idx)            

        idx+=1
    
        
    return ans