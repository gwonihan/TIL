try:
    age = int(input('나이를 입력하세요'))    # input 함수의 리턴값은 문자 이므로 숫자로
                                          # 바꿔주기위해 int (정수)를 사용한다.
    if age < 18:                          
        print('미성년자!!')
    else:
        print('환영합니다.')                
except Exception as e:
    print('입력이 정확하지 않습니다. :',e)

else:
    if age < 18:
        print('미성년자')
    else:
        print('환영합니다.')
