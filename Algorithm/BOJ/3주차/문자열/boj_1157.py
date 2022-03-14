n = input()

word_dic = {}
for i in n.lower():
    if i not in word_dic:
        word_dic[i] = 1
    else:
       word_dic[i] += 1 

word_max = [k for k,v in word_dic.items() if max(word_dic.values()) == v]
a = len(word_max)
if a >= 2:
    print("?")
else:
    print(word_max[0].upper())