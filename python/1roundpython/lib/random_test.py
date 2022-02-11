import random

# 실수형 난수
# print(random.random())

# 정수형 난수 (범위를 줘야함)
# print(random.randint(1, 10))

def random_pop(data):
    num = random.randint(0, len(data)-1)
    return data.pop(num)

# pop때문에 5번만 실행 됨
# data = [1,2,3,4,5]
# while data:
#     print(data)
#     print(random_pop(data))

def random_pop2(data):
    num = random.choice(data) #choice는 pop과같은역할!
    data.remove(num)
    return num

data = [1,2,3,4,5]
# while data:
#     print(data)
#     print(random_pop2(data))

random.shuffle(data)
print(data)
