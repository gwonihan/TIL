# [Errno 2] No such file or directory: 'xxx.txt'
# f = open('xxx.txt','r')

# ZeroDivisionError: division by zero
# print(4/0)

# IndexError: list index out of range
# a=[1,2,3]
# print(a[4])

# 예외(exception)처리
try:             
    a = [1,2,3]
    print(a[4])                            
    4/0                                        
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# except (ZeroDivisionError, IndexError) as e:      이렇게도 사용 가능
#     print(e)
                          #class 의 최상위는 object 클래스 이다.
except Exception as e:    #에러들도 클래스인데, 에러들의 최상위 클래스는 Exception 이므로
    print(e)              #except Exception 으로하면, 한번에 에러를 처리할 수 있다.      
print('Hello World')

# 인위적으로 Exception 발생시키기
class Bird:
    def fly(self):
        # raise NotImplementedError
        print('I can fly')

class Eagle(Bird):
    pass

eagle = Eagle()

eagle.fly()
