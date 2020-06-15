# random.choice

import random

# 초기 
nums = []
lottos = []
for i in range(1,46):
    nums.append(str(i))

# 번호 추출 함수 
def random_pop(data):
    num = random.choice(data)
    data.remove(num)
    return num

# 번호 추출 
for i in range(1,7):
    lottos.append(random_pop(nums))

# 번호 출력 
print(','.join(lottos))