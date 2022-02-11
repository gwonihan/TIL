#프로그램 실행할 때, 옵션 주기

import sys

# print(sys.argv[0])
# print(sys.argv[1])
try:
    if sys.argv[1] == 'call':
        print(sys.argv[1])
    elif sys.argv[1] == 'exit':
        sys.exit()
    elif sys.argv[1] == 'path':
        print(sys.path)
    elif sys.argv[1] == 'append_path':
        # print(sys.argv[2])
        sys.path.append(sys.argv[2])
        print(sys.path)    
    else:
     print('Not support')

except Exception as e:
    print('데이터 부족')

print('끝')