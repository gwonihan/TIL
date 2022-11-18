def add(a,b):
    return a + b

def sub(a,b):
    return a - b

print(__name__)

if __name__ == '__main__':            #mod1이 직접 실행 된다면, 출력
    print('==========',add(5,3))      #import 하여 사용하면 메인이 아니므로, 출력 안됨
    print('==========',sub(5,2))

    
