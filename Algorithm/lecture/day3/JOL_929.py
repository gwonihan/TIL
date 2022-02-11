n = int(input())
li = [f'No.{i}' for i in range(1,n+1)]
print(li)

# for i in range(1,n+1):
#     li.append(f'No.{i}')

# 두 가지 모두 가능, 하지만 f스트링이 빠름
# 'NO.' + str(i)
# f'NO.{f}'