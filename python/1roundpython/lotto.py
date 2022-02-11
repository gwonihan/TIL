# import random

# results = []

# while len(results) < 6:
#     num = random.randint(1,45)

#     if num not in results:
#         results.append(num)

# print(results)

import random
lotto = sorted(random.sample(range(1,46), 6))
print(lotto)
