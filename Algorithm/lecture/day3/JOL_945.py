# 딕셔너리 만들기
animation = {
    "Pkemon" : "Pikachu",
    "Digimon" : "Agumon",
    "Yugioh" : "Black Magician"
}

word = input()

# 세 개 중에 나오면 value / I don't know
if word in animation:
    print(animation[word])
else:
    print("I don't know")

# 위의 코드를 한줄로!
# print(animation.get(word, "I'dont know"))