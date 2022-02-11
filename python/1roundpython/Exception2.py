class MyError(Exception):             #Exception 클래스 상속받기
    # print('바보라고 부르지마')
    # pass
    def __str__(self):
       return '내가 정의한 에러'    

def say_nick(nick):
    if nick == '바보':
        raise MyError()

    print(nick)

# say_nick('바부')
say_nick('바보')

# try:
#     say_nick('바보')
# except Exception as e:
#     print(e)