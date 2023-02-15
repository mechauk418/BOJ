def solution(citations):
    citations = sorted(citations, reverse=True)
    for l in range(1, len(citations) + 1):
        cur = citations[l - 1]
        if (l == cur):
            return l
        elif (l > cur):
            return l - 1

    return len(citations)