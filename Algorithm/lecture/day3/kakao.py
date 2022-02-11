#숫자 문자열과 영단어


word_num = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

s = input()

for i,j in word_num.items():
    s = s.replace(i, j)
    

print(int(s))
    # s = s.replace(i, change)

# print(s) one4seveneight