# [1차] 뉴스 클러스터링
# 틀린 풀이

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    print(str1, str2)
    
    length = 2
    s1 = [str1[i:i+length]  for i in range(0, len(str1), length) if len(str1[i:i+length])==2 and str1[i:i+length].isalpha()]
    s2 = [str1[i:i+length] for i in range(1, len(str1), length) if len(str1[i:i+length])==2 and str1[i:i+length].isalpha()]
    str1 = s1 + s2
    print(str1)
    
    s3 = [str2[i:i+length]  for i in range(0, len(str2), length) if len(str2[i:i+length])==2 and str2[i:i+length].isalpha()]
    s4 = [str2[i:i+length] for i in range(1, len(str2), length) if len(str2[i:i+length])==2 and str2[i:i+length].isalpha()]
    str2 = s3 + s4
    print(str2)
    
    print(list(set(str1) & set(str2)))
    print(list(set(str1) | set(str2)))
    
    if len(str1) == 0:
        return 65536
    else:
        return len(list(set(str1) & set(str2))) / len(list(set(str1) | set(str2))) * 65536
    

# 참고풀이
from collections import Counter
def solution(str1, str2):
    
    arr1 = [str1[i:i + 2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    arr2 = [str2[i:i + 2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    if len(arr1) == 0 and len(arr2) == 0:
        return 65536
    
    c1 = Counter(arr1)
    c2 = Counter(arr2)
    # print("counter:", c1, c2)
    
    sum_li = sum((c1|c2).values())
    inter_li = sum((c1&c2).values())
    # print("list:", sum_li, inter_li)
    
    return int(inter_li / sum_li * 65536)