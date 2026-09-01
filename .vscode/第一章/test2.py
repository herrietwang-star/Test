import random


# 生成 30 个 1 到 100 之间的随机整数
random_numbers = [random.randint(1, 100) for _ in range(30)]

print("生成的 30 个随机数：")
print(random_numbers)
