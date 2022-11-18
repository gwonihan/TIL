nums = ['10.22','','8.00']

for num in nums:
    try:
        print(float(num))

    except Exception as e:
        print(0)

nums = ['10.22','','8.00']
li = []

for num in nums:
    try:
        li.append(float(num))

    except Exception as e:
        li.append(0)

print(li)