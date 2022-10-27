# H-Index
def solution(citations):
    
    citations.sort()
    centerIndex = len(citations) // 2
    
    while True:
        s = citations[centerIndex]
        if s <= len(citations[centerIndex:]):
            break
        else:
            centerIndex -= 122
    
    return s                                                                                                                                                                                                        