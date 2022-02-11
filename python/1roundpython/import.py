# import mod1
# import 모듈명
#print(mod1.add(3, 4))
#print(mod1.sub(4,2))    

# from 모듈명 import *
# from 모듈명 import 함수명, 변수     << 이 방법이 명시적이기 때문에, 추천!

# print(__name__)

# from mod1 import add, sub
# print(add(3,4))
# print(sub(4,2))

# import mod.mod2 as mod2   # 같은 폴더가 아니라면 .으로 폴더 경로를 지정해준다
# print(mod2.PI)

# a = mod2.Math1()          # 'a = ...' : 객체를 만들어서 a라는 변수에 넣어줌
# print(a.solv(2))          # 클래스 내의 메써드 호출!

# result = mod2.add(mod2.PI,2)
# print(result)

import sys
sys.path.append('C:\workspace\mod')
print(sys.path)
