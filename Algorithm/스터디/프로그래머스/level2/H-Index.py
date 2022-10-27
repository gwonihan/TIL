# H-Index
def solution(citations):
    citations.sort(reverse=True)
    
    h = 0
    for i in citations:
        if h >= i:
            return h
        else:
            h += 1
    else:
        return len(citations)                                                                                                                                                                                                      