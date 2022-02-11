# python sum.py 10 20 30 40
# 입력값을 모두 더해서 출력하는 것을 코딩

# import sys

# nums = sys.argv[1:]
# sum = 0
# for num in nums:
#     try:
#         sum += int(num)
#     except Exception as e:
#         print('숫자만 넣어주세요!!')
#         break

# print('현재까지 합계:', sum)

# import os

# result = os.popen('dir').read()
# print(result)

import os

# 1.디렉토리이동
os.chdir('D:\Workspace')
# 2.dir명령어 실행
result = os.popen('dir')
print(result.read())