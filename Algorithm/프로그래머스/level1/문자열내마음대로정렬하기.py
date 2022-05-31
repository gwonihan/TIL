# 문자열 내 마음대로 정렬하기

# 예시만 풀이됨..
# def solution(strings, n):
#     dic = {}
#     for i in strings:
#         dic[i[n:]] = i
#     dic = sorted(dic.items())
#     print(dic)
#     answer = []
#     for key, value in dic:
#         answer.append(value)
        
#     print(answer)
    
#     return answer

# 이뭔...
def solution(strings, n):
    strings.sort(key = lambda i: (i[n],i))
    return strings