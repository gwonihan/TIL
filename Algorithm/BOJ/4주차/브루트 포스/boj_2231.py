# 생성자




#분해합



# 지은님 풀이
# #i를 문자열로 만든 후 , 인덱싱을 이용해서 더하기..

# N = int(input())
# #n = int(N)

# jj_lst = []
# ii_lst = [] #생성자 목록
# i_lst = []
# #for i in range(len(N)):

# jj = 0
# #생성자(M)는 어차피  N보다 작다...
# for i in range(N):
#     jj = 0
#     ii = i
#     str_i = str(i)
#     for j in range(len(str_i)): #i의 자리수...
#         #자리수끼리 더한거
#         jj += int(str_i[j])

#     if jj < N:
#         if ii+jj == N:
#             ii_lst.append(ii)
#         else:
#             continue


# if ii_lst == []:
#     print(0)
# else:
#     print(min(ii_lst))
